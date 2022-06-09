from django.forms import ModelForm
from .models import dict
from django import forms

class dict_from(ModelForm):
    class Meta:
        model = dict
        fields = ['en_word', 'defn_word', 'type_word']

class login_form(forms.Form):
    get_username = forms.CharField(label='Your name', max_length=100)
    get_pass = forms.CharField(label='Your Password', max_length=100)