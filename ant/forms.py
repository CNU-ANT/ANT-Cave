from django import forms

from ant.models import UserInfo


class LoginForm(forms.Form):
    id = forms.CharField(required=True)
    password = forms.CharField(required=True)


class SignupForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        exclude = [
            'user',
        ]