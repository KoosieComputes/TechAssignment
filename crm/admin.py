from django.contrib import admin

from .models import Customer, Document


class DocumentInline(admin.TabularInline):
    extra = 0
    model = Document
    readonly_fields = ('type', 'uploaded_at', 'document', 'file_link',)
    exclude = ('mime_type',)
    fields = ('file_link',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('name', 'email', 'created_at')
    inlines = [DocumentInline]

    list_filter = ['created_at']
    search_fields = ['name']
