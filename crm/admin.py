from django.contrib import admin

from .models import Customer, Document


class DocumentInline(admin.TabularInline):
    extra = 0
    model = Document

    fields = ('download_link',)
    readonly_fields = ('type', 'uploaded_at', 'document', 'download_link',)
    exclude = ('mime_type',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('name', 'email', 'created_at')
    inlines = [DocumentInline]

    list_filter = ['created_at']
    search_fields = ['name']
