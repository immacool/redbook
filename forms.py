from django.forms import ModelForm
from .models import CaseFile


class CaseFileForm(ModelForm):
    class Meta:
        model = CaseFile
        fields = ['first_name', 'last_name']
