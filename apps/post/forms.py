from django import forms
from django.forms import widgets 

from .models import Post


class PostCreationForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required':'True'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'readonly': '',}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.SelectMultiple(attrs={'class': 'form-control'}),   
            'thumbnail': forms.FileInput(attrs={'class': 'form-control-file'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'required':'True'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'required':'True'}),
        }