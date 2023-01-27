from django import forms
from .models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document', )

    def is_valid(self):
        if not super().is_valid():
            return False
        if self.instance.document == 'NULL':
            return False

        return True
