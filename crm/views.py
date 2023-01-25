from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.urls import reverse

from .forms import DocumentForm
# from .functions import handle_uploaded_file


def HomeView(request):
    return render(request, 'crm/home.html')


def SuccessView(request):
    return render(request, 'crm/success.html')


def ProfileView(request):
    return render(request, 'crm/profile.html')


def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('crm:success'))
    else:
        form = DocumentForm()
    return render(request, 'crm/profile.html', {'form': form})
