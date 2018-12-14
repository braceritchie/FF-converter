from django import forms

class FileField(forms.Form):
    file = forms.ImageField()
