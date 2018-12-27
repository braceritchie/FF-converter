from django import forms

class AudFileField(forms.Form):
    audfile = forms.FileField(label="")
