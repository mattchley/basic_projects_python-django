from django import forms

class User_Form(forms.Form):
    user = forms.CharField(widget=forms.TextInput, label='Search Users', min_length=1)
    