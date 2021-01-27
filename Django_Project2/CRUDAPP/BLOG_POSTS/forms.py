from django import forms
from django.forms import ModelForm
from . models import blog_model



class blog_form(ModelForm):
    class Meta:
        model= blog_model
        fields= "__all__"

