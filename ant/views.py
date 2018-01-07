# coding=utf-8
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
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
def greetings_page(request):
    return render(request, 'greetings.html')


@login_required(login_url=LOGIN_URL)
def team_page(request):
    return render(request, 'team.html')


@login_required(login_url=LOGIN_URL)
def share_info_page(request):
    return render(request, 'share.html')


@login_required(login_url=LOGIN_URL)
def ant_algo_page(request):
    return render(request, 'ant_algo.html')


@login_required(login_url=LOGIN_URL)
def competition_algo_page(request):
    return render(request, 'competition_algo.html')


def find_id_page(request):
    return render(request, 'find_id.html')


def sign_up_page(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(username=form.cleaned_data['user_id'])
                return render(request, 'signup.html',{''})
                # 초기화되는 문제, 창을 띄울 것인지 화면에 글로 보일것인지의 문제
            except:
                pass
    else:
        form = SignupForm()
    return render(request, 'signup.html', locals())


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['id']
            password = form.cleaned_data['password']
            try:
                user_id = User.objects.get(username=user_id)
            except:
                id_err = u'아이디가 존재하지 않습니다.'
            user = authenticate(user_id=user_id, password=password)
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