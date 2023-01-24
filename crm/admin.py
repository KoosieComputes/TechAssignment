from django.contrib import admin

from .models import Customer, Document


class DocumentInline(admin.TabularInline):
    model = Document
    extra = 3


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    inlines = [DocumentInline]
    list_filter = ['created_at']
    search_fields = ['name']


admin.site.register(Customer, CustomerAdmin)
