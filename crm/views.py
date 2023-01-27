from django.http import HttpResponseRedirect, HttpResponse, FileResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse
from django.core.mail import send_mail

from .forms import DocumentForm
from .models import Customer, Document
from TechAssignment.settings import MEDIA_ROOT


def HomeView(request):
    return render(request, 'crm/home.html')


def ProfileView(request):
    form = DocumentForm()
    return render(request, 'crm/profile.html', {'form': form})


def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # Parse info from document post
            document = form.save(commit=False)
            mimetype = request.FILES['document'].content_type
            print(document.document)
            document.mime_type = mimetype
            document.save()
            return render(request, 'crm/profile.html', {'form': form, 'success': True})
    else:
        form = DocumentForm()
    return render(request, 'crm/profile.html', {'form': form})


def send_email(request):
    id = request.POST['customer_id']
    message = request.POST['message']

    customer = get_object_or_404(Customer, pk=id)
    send_mail(
        'Document Request',
        message,
        # TODO: pull email and name from authenticated user
        'Cobus Theunissen <rmcobus@futureforex.co.za>',
        [f'{customer.name} <{customer.email}>'],
        fail_silently=False,
    )
    return HttpResponseRedirect(reverse('admin:crm_customer_changelist'))


def download(request):
    document = get_object_or_404(Document, pk=request.GET.get('id'))
    filepath = MEDIA_ROOT / str(document.document)
    print(filepath)
    response = FileResponse(open(filepath, 'rb'),
                            content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=%s' % str(
        document.document)

    return response
