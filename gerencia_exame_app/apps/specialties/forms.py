from django import forms
from .models import Specialty

class SpecialtyForm(forms.ModelForm):

    class Meta:
        model = Specialty
        exclude = ('created_on' , 'updated_on',)