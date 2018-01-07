"""ANTCave URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from ant import views as ant_site

urlpatterns = [
    url(r'^$', ant_site.main_page, name='main'),
    url(r'pedigree/$', ant_site.pedigree_page, name='pedigree'),
    url(r'greetings/$', ant_site.greetings_page, name='greetings'),
    url(r'team/$', ant_site.team_page, name='team'),
    url(r'share/$', ant_site.share_info_page, name='share'),
    url(r'ant_algo/$', ant_site.ant_algo_page, name='ant_algo'),
    url(r'compet_algo/$', ant_site.competition_algo_page, name='compet_algo'),
    url(r'find/$', ant_site.find_id_page, name='find_id'),
    url(r'signup/$', ant_site.sign_up_page, name='sign_up'),
    url(r'login/$', ant_site.login_page, name='login'),
    url(r'^admin/', admin.site.urls),
]
