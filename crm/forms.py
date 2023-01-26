from django import forms
from .models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('customer', 'document', )


class SendRequestForm(forms.Form):
    message = forms.CharField(
        label='Message', widget=forms.Textarea)
