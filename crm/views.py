from django.http import HttpResponseRedirect, HttpResponse, FileResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

from .forms import DocumentForm
from .models import Customer, Document
from TechAssignment.settings import MEDIA_ROOT, DEFAULT_FROM_EMAIL


def HomeView(request):
    return render(request, 'crm/home.html')


def ProfileView(request):
    form = DocumentForm()
    return render(request, 'crm/profile.html', {'form': form})


def upload_file(request):
    if request.method == 'GET':
        # Find user from token
        token = request.GET.get('token')
        try:
            customer = Customer.objects.get(token=token)
        except Customer.DoesNotExist():
            return HttpResponseNotFound()
        form = DocumentForm()
        data = {'form': form, 'customer': customer}

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        customer = Customer.objects.get(pk=request.POST["id"])
        if form.is_valid():
            # Parse info from document post
            document = form.save(commit=False)
            mimetype = request.FILES['document'].content_type
            document.mime_type = mimetype
            document.customer_id = request.POST["id"]
            document.save()
            data = {
                'form': form, 'feedback': "File uploaded successfully", 'customer': customer}
            message = f'{customer.name} has uploaded the following document: {document.document}'
            # TODO: find clients manager
            send_mail(
                'Document Uploaded',
                message,
                'System FutureForex <no-reply@futureforex.co.za>',
                [DEFAULT_FROM_EMAIL],
                fail_silently=True,
            )
        else:
            data = {
                'form': form, 'feedback': "Please select a file and try again", 'customer': customer}

    return render(request, 'crm/profile.html', data)


def send_email(request):
    id = request.POST['customer_id']
    message = request.POST['message']
    customer = get_object_or_404(Customer, pk=id)
    link = request.build_absolute_uri(f'/upload/?token={customer.token}')
    message_with_link = message + '\n\n' + link
    send_mail(
        'Document Request',
        message_with_link,
        # TODO: pull email and name from authenticated user
        None,
        [f'{customer.name} <{customer.email}>'],
        fail_silently=False,
    )
    return HttpResponseRedirect(reverse('admin:crm_customer_changelist'))


@login_required
def download(request):
    document = get_object_or_404(Document, pk=request.GET.get('id'))
    filepath = MEDIA_ROOT / str(document.document)
    print(filepath)
    response = FileResponse(open(filepath, 'rb'),
                            content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=%s' % str(
        document.document)

    return response
