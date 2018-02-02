import os
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, tokens
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.http import is_safe_url
from ANTCave.settings import LOGIN_URL, BASE_DIR
from Profile.models import UserInfo
from .forms import LoginForm, SignupForm, FindIDForm, FindPasswordForm, ChangePasswordForm, EditInfoForm


@login_required(login_url=LOGIN_URL)
def user_logout(request):
    logout(request)
    return redirect('/')


@login_required(login_url=LOGIN_URL)
def edit_my_page(request):
    if request.method == 'POST':
        form = EditInfoForm(request.POST)
        if form.is_valid():
            try:
                user_info = UserInfo.objects.get(user=request.user)
                user_info.user_name = form.cleaned_data.get('name')
                user_info.user_phone = form.cleaned_data.get('phone')
                user_info.is_attend = form.cleaned_data.get('is_attend')
                user_info.save()
                return render(request, 'profile/my_page.html', locals())
            except:
                pass
        return redirect('/')
    # FIXME : 회원정보 수정 시 db가 update 되지 않아서 빈칸으로 나옴.
    user_info = UserInfo.objects.get(user=request.user)
    form = EditInfoForm(
        initial={
            'name':user_info.user_name,
            'phone':user_info.user_phone,
            'is_attend':user_info.is_attend,
        }
    )
    return render(request, 'profile/edit_info.html', locals())


@login_required(login_url=LOGIN_URL)
def my_page(request):
    user_info = UserInfo.objects.get(user=request.user)
    if user_info.is_attend == 'a':
        is_attend = '재학'
    elif user_info.is_attend == 'l':
        is_attend = '휴학'
    else:
        is_attend = '졸업'
    return render(request, 'profile/my_page.html', locals())


def find_id_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = FindIDForm(request.POST)
        if form.is_valid():
            try:
                user_info = UserInfo.objects.get(user_num=form.cleaned_data.get('num'))
                user_id = user_info.user.username
                response = '회원님의 ID는'+ user_id +'입니다.'

            except:
                response = '해당 학번의 ID가 존재하지 않습니다.'
        return render(request, 'profile/find_id.html', locals())
    form = FindIDForm()
    return render(request, 'profile/find_id.html', locals())


def find_password_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = FindPasswordForm(request.POST)
        if form.is_valid():
            try:
                form = ChangePasswordForm(
                    initial={
                        'id':User.objects.get(username=form.cleaned_data.get('id')).username
                    }
                )
                return render(request, 'profile/change_password.html', locals())
            except:
                response = '존재하지 않는 ID입니다.'
        return render(request, 'profile/find_password.html', locals())
    form = FindPasswordForm()
    return render(request, 'profile/find_password.html', locals())


def change_password_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            if not form.cleaned_data.get('password') == form.cleaned_data.get('password_confirm'):
                response = '비밀번호가 일치하지 않습니다'
                return render(request, 'profile/signup.html', locals())
            user = User.objects.get(username=form.cleaned_data.get('id'))
            user.set_password(form.cleaned_data.get('password'))
            user.save()
    return redirect('/')


def sign_up_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            try:
                User.objects.get(username=form.cleaned_data.get('id'))
                response = 'id가 이미 존재합니다.'
                return render(request, 'profile/signup.html', locals())
                # 초기화되는 문제, 창을 띄울 것인지 화면에 글로 보일것인지의 문제
            except:
                pass
            if not form.cleaned_data.get('password') == form.cleaned_data.get('password_confirm'):
                response = '비밀번호가 일치하지 않습니다'
                return render(request, 'profile/signup.html', locals())
            try:
                User.objects.get(email=form.cleaned_data.get('email'))
                response = '가입된 email이 이미 존재합니다.'
                return render(request, 'profile/signup.html', locals())
            except:
                pass

            user_info = UserInfo()
            try:
                user_info.user_name = form.cleaned_data.get('name')
                user_info.user_num = form.cleaned_data.get('num')
                user_info.user_phone = form.cleaned_data.get('phone')
                user_info.is_attend = form.cleaned_data.get('is_attend')
            except:
                return render(request, 'profile/signup.html', locals())
            new_user = User.objects.create_user(
                username=form.cleaned_data.get('id'),
                password=form.cleaned_data.get('password'),
                email=form.cleaned_data.get('email'),
            )
            new_user.save()
            user_info.user = new_user
            user_info.save()
            # # 이메일 인증 필요
            #
            # user = authenticate(
            #     username=form.cleaned_data.get('id'),
            #     password=form.cleaned_data.get('password'),
            # )

            # messages.add_message(request, messages.SUCCESS, '가입을 환영합니다.')
            return redirect('/')
    form = SignupForm()
    return render(request, 'profile/signup.html', locals())


def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data.get('id')
            password = form.cleaned_data.get('password')
            try:
                login_user = User.objects.get(username=user_id)
            except:
                response = '아이디가 존재하지 않습니다.'
                return render(request, 'profile/login_page.html', locals())
            login_user = authenticate(username=user_id, password=password)
            if login_user is not None:
                user_info = UserInfo.objects.get(user=login_user)
                # if user_info.level == 0:
                #     response = '이메일 인증이 되지 않은 계정입니다.'
                #     return render(request, 'profile/login_page.html', locals())
                login(request, user=login_user)
                return redirect('/')
            else:
                response = '비밀번호가 잘못되었습니다.'
        return render(request, 'profile/login_page.html', locals())
    form = LoginForm()
    return render(request, 'profile/login_page.html', locals())


def user_active_page(request):
    domain = '127.0.0.1/'
    return render(request, 'profile/user_active.html', locals())
