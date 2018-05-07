from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from ANTCave.settings import LOGIN_URL
from Board.views import IndexView, ContentView, EditView, NewView

app_name = 'board'
urlpatterns = [
    url('^$', IndexView.as_view(), name='board',),
    url('^(?P<pk>\d+)/$', ContentView.as_view(), name='detail'),
    url('^edit/$', csrf_exempt(login_required(EditView.as_view(), login_url=LOGIN_URL)), name='edit'),
    url('^new/$', csrf_exempt(login_required(NewView.as_view(), login_url=LOGIN_URL)), name='new'),
]