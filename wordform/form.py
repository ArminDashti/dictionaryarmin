from django import forms

class nameform(forms.Form):
    subject = forms.CharField(max_length=100, initial='write your subject')
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)