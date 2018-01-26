from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ANTCave.settings import LOGIN_URL
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
