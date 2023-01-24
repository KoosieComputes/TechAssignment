from django.db import models
from django.contrib import admin
from django.utils import timezone

import datetime


class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField("date registered")


class Document(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    filename = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    mime_type = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField()
