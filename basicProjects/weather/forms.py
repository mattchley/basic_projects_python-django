from django import forms

class Weather_Form(forms.Form):
    location = forms.CharField(widget=forms.TextInput, label='Search City', min_length=1, max_length=100)
    