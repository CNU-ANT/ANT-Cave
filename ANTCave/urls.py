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
    url(r'pedigree/(?P<pk>\d+)/$', ant_site.pedigree_page, name='pedigree_detail'),
    url(r'greetings/$', ant_site.greetings_page, name='greetings'),
    url(r'greetings/(?P<pk>\d+)/$', ant_site.greetings_detail_page, name='greetings_detail'),
    url(r'team/$', ant_site.team_page, name='team'),
    url(r'team/(?P<pk>\d+)/$', ant_site.team_detail_page, name='team_detail'),
    url(r'share/$', ant_site.share_info_page, name='share'),
    url(r'share/(?P<pk>\d+)/$', ant_site.share_detail_page, name='share_detail'),
    url(r'ant_algo/$', ant_site.ant_algo_page, name='ant_algo'),
    url(r'ant_algo/(?P<pk>\d+)/$', ant_site.ant_algo_detail_page, name='ant_algo_detail'),
    url(r'compete_algo/$', ant_site.competition_algo_page, name='compete_algo'),
    url(r'compete_algo/(?P<pk>\d+)/$', ant_site.competition_algo_detail_page, name='compete_algo_detail'),
    url(r'find/$', ant_site.find_id_page, name='find_id'),
    url(r'signup/$', ant_site.sign_up_page, name='sign_up'),
    url(r'login/$', ant_site.login_page, name='login'),
    url(r'confirm_id/$', ant_site.confirm_id, name='confirm_id'),
    url(r'^admin/', admin.site.urls),
]