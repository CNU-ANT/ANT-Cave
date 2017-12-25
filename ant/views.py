from django.shortcuts import render


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