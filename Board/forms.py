from django import forms
from django.forms import Textarea, FileField

from Board.models import TeamPost


class PostForm(forms.Form):
    title = forms.CharField(
        max_length=30,
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '제목 입력',
            }
        ),
        required=True,
    )
    text = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': '내용 입력',
            }
        ),
        required=True,
    )
    file = FileField(
        label='파일',
        required=False,
        widget=forms.ClearableFileInput(
            attrs={'multiple': True}
        )
    )
    # class Meta:
    #     model = TeamPost
    #     fields = ('title', 'text',)
    #     widgets = {
    #         'title': Textarea(
    #             attrs= {
    #                 'class': 'form-control',
    #                 'placeholder':'제목을 입력해주세요.',
    #             }
    #         ),
    #         'text': Textarea(
    #             attrs={
    #                 'class': 'form-control',
    #             }
    #         )
    #     }


class LabelForm(forms.Form):
    pass


class CommentForm(forms.Form):
    text = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': '내용 입력',
            }
        ),
        required=True,
    )
