from django import forms
from .models import Exam

class ExamForm(forms.ModelForm):

    class Meta:
        model = Exam
        exclude = ('created_on' , 'updated_on',)