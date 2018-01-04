from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from .forms import LoginForm


# Create your views here.
def main_page(request):
    return render(request, 'main.html')


def pedigree_page(request):
    return render(request, 'pedigree.html')


def greetings_page(request):
    return render(request, 'greetings.html')


def team_page(request):
    return render(request, 'team.html')


def share_info_page(request):
    return render(request, 'share.html')


def ant_algo_page(request):
    return render(request, 'ant_algo.html')


def competition_algo_page(request):
    return render(request, 'competition_algo.html')


def sign_up_page(request):
    return render(request, 'signup.html')


def login_page(request):
    previous_page = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        if is_safe_url(url=previous_page):
            return redirect(previous_page)
        else:
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'login_page.html', locals())