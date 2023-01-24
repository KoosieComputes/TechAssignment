from django.shortcuts import render
from django.views import generic
from django.urls import reverse


def HomeView(request):
    return render(request, 'customer/home.html')
