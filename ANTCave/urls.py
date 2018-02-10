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
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from Profile import views as profile
from Board import views as board
from Board import models

urlpatterns = [
    url(r'^$', board.main_page, name='main'),
    url(r'^pedigree/$', board.pedigree_page, name='pedigree'),
    url(r'^pedigree/', include('Board.urls', namespace='pedigree'),
        {
            'b_name': '족보 게시판',
            'b_name_e': 'Pedigree page',
            'namespace':'pedigree',
            'post': models.PedigreePost(),
            'comment': models.PedigreeComment(),
            'label': models.PedigreeLabel(),
        },
    ),
    url(r'^greetings/', include('Board.urls', namespace='greetings'),
        {
            'b_name': '가입 인사',
            'b_name_e': 'Greetings page',
            'namespace':'greetings',
            'post': models.GreetingsPost(),
            'comment': models.GreetingsComment(),
            'label': models.GreetingsLabel(),
        },
    ),
    url(r'^team/', include('Board.urls', namespace='team'),
        {
            'b_name': '팀 게시판',
            'b_name_e': 'Team page',
            'namespace':'team',
            'post': models.TeamPost(),
            'comment': models.TeamComment(),
            'label': models.TeamLabel(),
        },
    ),
    url(r'^share/', include('Board.urls', namespace='share'),
        {
            'b_name': '정보공유 게시판',
            'b_name_e': 'Share Info page',
            'namespace':'share',
            'post': models.ShareInfoPost(),
            'comment': models.ShareInfoComment(),
            'label': models.ShareInfoLabel(),
        },
    ),
    url(r'^algorithm/ant/', include('Board.urls', namespace='ant_algo'),
        {
            'b_name': 'ANT 문제 게시판',
            'b_name_e': 'ANT Algorithm page',
            'namespace':'ant_algo',
            'post': models.ANTAlgorithmPost(),
            'comment': models.ANTAlgorithmComment(),
            'label': models.ANTAlgorithmLabel(),
        },
    ),
    url(r'^algorithm/competition/', include('Board.urls', namespace='compete_algo'),
        {
            'b_name': '대회 문제 게시판',
            'b_name_e': 'Algorithm page',
            'namespace':'compete_algo',
            'post': models.CompetitionPost(),
            'comment': models.CompetitionComment(),
            'label': models.CompetitionLabel(),
        },
    ),
    url(r'^find_id/$', profile.find_id_page, name='find_id'),
    url(r'^find_password/$', profile.find_password_page, name='find_password'),
    url(r'^change_password/$', profile.change_password_page, name='change_password'),

    url(r'^my_page/$', profile.my_page, name='my_page'),
    url(r'^my_page/edit/$', profile.edit_my_page, name='edit_my_page'),

    url(r'^signup/$', profile.sign_up_page, name='sign_up'),
    url(r'^active/$', profile.user_active_page, name='user_active'),
    url(r'^login/$', profile.login_page, name='login'),
    url(r'^logout/$', profile.user_logout, name='logout'),

    url(r'^admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
