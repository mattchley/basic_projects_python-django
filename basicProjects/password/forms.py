from django import forms

class Password_Form(forms.Form):
    length = forms.IntegerField(min_value=12, max_value=128)
    letters = forms.BooleanField(required=False)
    numbers = forms.BooleanField(required=False)
    symbols = forms.BooleanField(required=False)
    capitalization = forms.BooleanField(required=False)