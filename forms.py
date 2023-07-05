from django import forms
from .models import *

class CommentForms(forms.ModelForm):
    class Meta:
        model = Addcommentaire
        fields = ['content']
        labels = {'content':'commentaire'}
        widgets= {
            'content': forms.Textarea(attrs={'class': 'form-control'})
        }

