from django import forms
from ant.models import UserInfo


class LoginForm(forms.Form):
    id = forms.CharField(required=True)
    password = forms.CharField(required=True)


class IdForm(forms.Form):
    id = forms.CharField(max_length=20, required=True)


class SignupForm(forms.Form):
    id = forms.CharField(
        max_length=20,
        label='ID',
        widget=forms.TextInput(
            attrs={'class':'form-control',
                   'placeholder':'아이디를 입력해주세요.',
                   'required':True,
        }),
        required=True,
    )
    password = forms.CharField(
        max_length=20,
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={'class':'form-control',
                   'placeholder':'비밀번호를 입력해주세요.',
                   'required': True,

            }),
        required=True,
    )
    password_confirm = forms.CharField(
        max_length=20,
        label='비밀번호 확인',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': '비밀번호를 다시 입력해주세요.',
                   'required': True,

                   }),
        required=True,
    )
    email = forms.EmailField(
        label='이메일',
        widget=forms.EmailInput(
            attrs={'class':'form-control',
                   'placeholder':'이메일을 입력해주세요.',
                   'required':True,
            }),
        required=True,
    )
    name = forms.CharField(
        max_length=10,
        label='이름',
        widget=forms.TextInput(
            attrs={'class':'form-control',
                   'placeholder':'이름을 입력해주세요. ex) 서영학',
                   'required': True,
            }),
        required=True,
    )
    num = forms.CharField(
        max_length=10,
        label='학번',
        widget=forms.TextInput(
            attrs={'class':'form-control',
                   'placeholder':'201800000 식으로 입력해주세요.',
                   'minlength': 9,
                   'maxlength': 9,
                   'required': True,
            }),
        required=True,
    )
    phone = forms.CharField(
        max_length=15,
        label='전화번호',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder':'- 없이 숫자만 입력해주세요.',
                'maxlength':15,
                'minlength':10,
                'required': True,
            }),
        required=True,
    )
    is_attend = forms.ChoiceField(
        label='재학 여부 (시간이 지나면 관리자에 의해 변경될 수 있습니다.)',
        widget=forms.Select(
            attrs={
                'class':'form-control',
                'style':'width:200px;',
                'required': True,
            },
        ),
        choices=(
            ('a', '재학',),
            ('l', '휴학',),
            ('g', '졸업',),
        ),
        required=True,
    )
    # class Meta:
    #     model = UserInfo
    #     exclude = [
    #         'user',
    #     ]

