from django import forms
from .models import List

class Form(forms.ModelForm):
    class Meta:
        model = List
        fields = ('title', 'content', 'end_date')

