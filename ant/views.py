from datetime import datetime
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.http import is_safe_url

from ANTCave.settings import LOGIN_URL
from ant.models import UserInfo
from .forms import LoginForm, SignupForm, FindIDForm, FindPasswordForm, ChangePasswordForm


# Create your views here.
@login_required(login_url=LOGIN_URL)
def main_page(request):
    return render(request, 'main.html')


@login_required(login_url=LOGIN_URL)
def pedigree_page(request):
    return render(request, 'board/pedigree.html')


@login_required(login_url=LOGIN_URL)
def pedigree_detail_page(request, pk):
    # TODO : 입력으로 줄 모델을 만들어야 합니다.
    return render(request, 'board/pedigree_detail.html', locals())


@login_required(login_url=LOGIN_URL)
def greetings_page(request):
    return render(request, 'board/greetings.html')


@login_required(login_url=LOGIN_URL)
def greetings_detail_page(request, pk):
    # TODO : 입력으로 줄 모델을 만들어야 합니다.
    return render(request, 'board/greetings_detail.html', locals())


@login_required(login_url=LOGIN_URL)
def team_page(request):
    return render(request, 'board/team.html')


@login_required(login_url=LOGIN_URL)
def team_detail_page(request, pk):
    # TODO : 입력으로 줄 모델을 만들어야 합니다.
    return render(request, 'board/team_detail.html', locals())


@login_required(login_url=LOGIN_URL)
def share_info_page(request):
    return render(request, 'board/share.html')


@login_required(login_url=LOGIN_URL)
def share_detail_page(request, pk):
    # TODO : 입력으로 줄 모델을 만들어야 합니다.
    return render(request, 'board/share_detail.html', locals())


@login_required(login_url=LOGIN_URL)
def ant_algo_page(request):
    return render(request, 'board/ant_algo.html')


@login_required(login_url=LOGIN_URL)
def ant_algo_detail_page(request, pk):
    # TODO : 입력으로 줄 모델을 만들어야 합니다.
    return render(request, 'board/ant_algo_detail.html', locals())


@login_required(login_url=LOGIN_URL)
def competition_algo_page(request):
    return render(request, 'board/competition_algo.html')


@login_required(login_url=LOGIN_URL)
def competition_algo_detail_page(request, pk):
    # TODO : 입력으로 줄 모델을 만들어야 합니다.
    return render(request, 'board/competition_algo_detail.html', locals())


@login_required(login_url=LOGIN_URL)
def user_logout(request):
    logout(request)
    return redirect('/')


def find_id_page(request):
    if request.method == 'POST':
        form = FindIDForm(request.POST)
        if form.is_valid():
            try:
                user = UserInfo.objects.get(user_num=form.cleaned_data.get('num'))
                user_id = user.user.username
                response = '회원님의 ID는'+ user_id +'입니다.'

            except:
                response = '해당 학번의 ID가 존재하지 않습니다.'
        return render(request, 'user/find_id.html', locals())
    form = FindIDForm()
    return render(request, 'user/find_id.html', locals())


def find_password_page(request):
    if request.method == 'POST':
        form = FindPasswordForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(username=form.cleaned_data.get('id'))

                form = ChangePasswordForm()
                form.cleaned_data['id'] = user.username
                return render(request, 'user/change_password.html', locals())
            except:
                response = '존재하지 않는 ID입니다.'
        return render(request, 'user/find_password.html', locals())
    form = FindPasswordForm()
    return render(request, 'user/find_password.html', locals())


def change_password_page(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(username=form.cleaned_data.get('id'))

            except:
                response = '비밀번호가 일치하지 않습니다'
            return render(request, 'user/change_password.html', locals())
    return redirect('/')


def sign_up_page(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(username=form.cleaned_data.get('id'))
                response = 'id가 이미 존재합니다.'
                return render(request, 'user/signup.html', locals())
                # 초기화되는 문제, 창을 띄울 것인지 화면에 글로 보일것인지의 문제
            except:
                pass
            if not form.cleaned_data.get('password') == form.cleaned_data.get('password_confirm'):
                response = '비밀번호가 일치하지 않습니다'
                return render(request, 'user/signup.html', locals())
            try:
                user = User.objects.get(email=form.cleaned_data.get('email'))
                response = '가입된 email이 이미 존재합니다.'
                return render(request, 'user/signup.html', locals())
            except:
                pass
            try:
                user = UserInfo.objects.get(user_num=form.cleaned_data.get('num'))
                response = '이미 가입된 학번입니다.'
                return render(request, 'user/signup.html', locals())
            except:
                pass
            # user_info = UserInfo()
            # try:
            #     user_info.user_name = form.cleaned_data.get('name')
            #     user_info.user_num = form.cleaned_data.get('num')
            #     user_info.user_phone = form.cleaned_data.get('phone')
            #     user_info.is_attend = form.cleaned_data.get('is_attend')
            # except:
            #     return render(request, 'signup.html', locals())
            # user = User.objects.create_user(
            #     username=form.cleaned_data.get('id'),
            #     password=form.cleaned_data.get('password'),
            #     email=form.cleaned_data.get('email'),
            # )
            # user.save()
            # user_info.user = user
            # user_info.save()
            # # 이메일 인증 필요
            #
            # user = authenticate(
            #     username=form.cleaned_data.get('id').encode('utf8'),
            #     password=form.cleaned_data.get('password').encode('utf8'),
            # )
            # login(request, user=user)
            # messages.add_message(request, messages.SUCCESS, '가입을 환영합니다.')
            return redirect('/')
    form = SignupForm()
    return render(request, 'user/signup.html', locals())


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data.get('id')
            password = form.cleaned_data.get('password')
            try:
                user = User.objects.get(username=user_id)
            except:
                response = '아이디가 존재하지 않습니다.'
                return render(request, 'user/login_page.html', locals())
            user = authenticate(username=user_id, password=password)
            if user is not None:
                user_info = UserInfo.objects.get(user=user)
                # if user.is_active:
                try:
                    login(request, user=user)
                    return redirect('/')
                except:
                    response = '비밀번호가 잘못되었습니다.'
                    return render(request, 'user/login_page.html', locals())
            else:
                response = '아이디가 존재하지 않습니다.'
        return render(request, 'user/login_page.html', locals())
    form = LoginForm()
    return render(request, 'user/login_page.html', locals())
