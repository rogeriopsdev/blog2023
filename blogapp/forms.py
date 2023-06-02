from django import  forms
from .models import Tema, Post

class TemaForms(forms.ModelForm):
    class Meta:
        model = Tema
        fields ='__all__'

