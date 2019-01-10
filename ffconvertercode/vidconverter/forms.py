from django import forms

class VidFileField(forms.Form):
    file1 = forms.FileField(label="",widget=forms.ClearableFileInput(attrs={'multiple': True})) 