from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from django.core.validators import FileExtensionValidator

import datetime
import hashlib


class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField("date registered")
    token = models.CharField(max_length=255, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.token = hashlib.md5(self.email.encode("utf-8")).hexdigest()
        super().save(*args, **kwargs)


class Document(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    mime_type = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    document = models.FileField(upload_to='documents/', default='NULL', validators=[
                                FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'jpg', 'png'])])

    def __str__(self):
        return self.type

    def save(self, *args, **kwargs):
        self.mime_type = self.document.file.content_type
        super().save(*args, **kwargs)

    def download_link(self):
        if self.document:
            return format_html("<a href='/download?id=%s'>download</a>" % (self.pk,))
        else:
            return "No attachment"
    download_link.allow_tags = True
