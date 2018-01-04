from django import forms


class LoginForm(forms.Form):
    id = forms.CharField(required=True)
    password = forms.CharField(required=True)

