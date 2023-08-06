from django import forms
from .models import Outage

class OutageForm(forms.ModelForm):
    class Meta:
        model = Outage
        fields = ['ward_number', 'date']
