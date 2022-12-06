from django import forms
from .models import article

class articleForms(forms.ModelForm):
    class Meta:
        model = article
        fields = ['title','content','artimg']