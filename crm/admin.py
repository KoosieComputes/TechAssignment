from django.contrib import admin

from .models import Customer, Document


def list_doctypes():
    doc_types = []
    for doc in Document.objects.all():
        doc_types.append(doc.type)
    return list(filter(lambda val: val != '', doc_types))


class DocumentInline(admin.TabularInline):
    extra = 0
    model = Document

    fields = ('download_link', 'uploaded_at', 'type')
    readonly_fields = ('type', 'uploaded_at', 'document', 'download_link',)
    exclude = ('mime_type',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('name', 'email', 'created_at')
    inlines = [DocumentInline]

    list_filter = ['created_at']
    search_fields = ['name']

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['doctypes'] = list_doctypes()
        return super().change_view(request, object_id, form_url, extra_context=extra_context)
