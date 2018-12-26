from django import forms

class ActFileField(forms.Form):
    file1 = forms.FileField(label="",widget=forms.ClearableFileInput(attrs={'multiple': True})) 