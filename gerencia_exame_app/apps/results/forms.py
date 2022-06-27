from django import forms
from .models import Result, Patient, ResultItem, Exam

class ResultForm(forms.ModelForm):
    
    class Meta:
        model = Result
        exclude = ('patient', 'created_on' , 'updated_on')

class ResultItemForm(forms.ModelForm):
    
    class Meta:
        model = ResultItem
        exclude = ('result', 'created_on' , 'updated_on')
