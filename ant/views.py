from datetime import datetime
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.http import is_safe_url

from ANTCave.settings import LOGIN_URL
from ant.models import UserInfo
from .forms import LoginForm, SignupForm


# Create your views here.
@login_required(login_url=LOGIN_URL)
def main_page(request):
    return render(request, 'main.html')


@login_required(login_url=LOGIN_URL)
def pedigree_page(request):
    return render(request, 'pedigree.html')


@login_required(login_url=LOGIN_URL)
def pedigree_detail_page(request, pk):
    # TODO : 입력으로 줄 모델을 만들어야 합니다.
    return render(request, 'pedigree_detail.html', locals())


@login_required(login_url=LOGIN_URL)
def greetings_page(request):
    return render(request, 'greetings.html')


@login_required(login_url=LOGIN_URL)
def greetings_detail_page(request, pk):
    # TODO : 입력으로 줄 모델을 만들어야 합니다.
    return render(request, 'greetings_detail.html', locals())


@login_required(login_url=LOGIN_URL)
def team_page(request):
    return render(request, 'team.html')


@login_required(login_url=LOGIN_URL)
def team_detail_page(request, pk):
    # TODO : 입력으로 줄 모델을 만들어야 합니다.
    return render(request, 'team_detail.html', locals())


@login_required(login_url=LOGIN_URL)
def share_info_page(request):
    return render(request, 'share.html')


@login_required(login_url=LOGIN_URL)
def share_detail_page(request, pk):
    # TODO : 입력으로 줄 모델을 만들어야 합니다.
    return render(request, 'share_detail.html', locals())


@login_required(login_url=LOGIN_URL)
def ant_algo_page(request):
    return render(request, 'ant_algo.html')


@login_required(login_url=LOGIN_URL)
def ant_algo_detail_page(request, pk):
    # TODO : 입력으로 줄 모델을 만들어야 합니다.
    return render(request, 'ant_algo_detail.html', locals())


@login_required(login_url=LOGIN_URL)
def competition_algo_page(request):
    return render(request, 'competition_algo.html')


@login_required(login_url=LOGIN_URL)
def competition_algo_detail_page(request, pk):
    # TODO : 입력으로 줄 모델을 만들어야 합니다.
    return render(request, 'competition_algo_detail.html', locals())


@login_required(login_url=LOGIN_URL)
def user_logout(request):
    logout(request)
    return redirect('/')


def find_id_page(request):
    return render(request, 'find_id.html')


def sign_up_page(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(username=form.cleaned_data.get('user_id'))
                id_err = u'id가 이미 존재합니다.'
                return render(request, 'signup.html', locals())
                # 초기화되는 문제, 창을 띄울 것인지 화면에 글로 보일것인지의 문제
            except:
                user = User.objects.create_user(
                    username=form.cleaned_data.get('id'),
                    password=form.cleaned_data.get('password'),
                    email=form.cleaned_data.get('email'),
                )
                user.save()
                user_info = UserInfo()
                user_info.user = user
                user_info.user_name = form.cleaned_data.get('name')
                user_info.user_num = form.cleaned_data.get('num')
                user_info.user_phone = form.cleaned_data.get('phone')
                user_info.signup_date = datetime.today().strftime('%Y %m %d')
                user_info.save()
                # 이메일 인증 필요

                user = authenticate(
                    username=form.cleaned_data.get('id').encode('utf8'),
                    password=form.cleaned_data.get('password').encode('utf8'),
                )
                login(request, user=user)
                # messages.add_message(request, messages.SUCCESS, '가입을 환영합니다.')
                return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', locals())


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data.get('id')
            password = form.cleaned_data.get('password')
            try:
                user = User.objects.get(username=user_id)
            except:
                id_err = u'아이디가 존재하지 않습니다.'
                return render(request, 'login_page.html', locals())
            user = authenticate(username=user_id, password=password)
            if user is not None:
                user_info = UserInfo.objects.get(user=user)
                # if user.is_active:
                try:
                    login(request, user=user)
                    return redirect('/')
                except:
                    pw_err = u'비밀번호가 잘못되었습니다.'
                    return render(request, 'login_page.html', locals())
            else:
                id_err = u'아이디가 존재하지 않습니다.'
        return render(request, 'login_page.html', locals())
    else:
        form = LoginForm()
    return render(request, 'login_page.html', locals())