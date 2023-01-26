from django.contrib import admin

from .models import Customer, Document
from .forms import SendRequestForm


class DocumentInline(admin.TabularInline):
    extra = 0
    model = Document
    readonly_fields = ('filename', 'uploaded_at', 'document',)
    exclude = ('mime_type', 'path',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('name', 'email', 'created_at')
    inlines = [DocumentInline]

    list_filter = ['created_at']
    search_fields = ['name']
