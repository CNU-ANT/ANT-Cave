from django import forms
from ant.models import UserInfo


class LoginForm(forms.Form):
    id = forms.CharField(required=True)
    password = forms.CharField(required=True)


class SignupForm(forms.Form):
    id = forms.CharField(max_length=20, required=True)
    password = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=10)
    num = forms.CharField(max_length=10)
    phone = forms.CharField(max_length=15)
    # class Meta:
    #     model = UserInfo
    #     exclude = [
    #         'user',
    #     ]