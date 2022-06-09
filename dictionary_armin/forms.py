from django.forms import ModelForm
from django import forms
from .models import words

class insert_word_form(ModelForm):
    class Meta:
        model = words
        fields = ['english_word', 'english_meaning']