from django.conf.urls import url, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'board'

urlpatterns = [
    url(r'^$', views.board.as_view(), name='board'),
    url(r'^insert/$', views.check_post, name='board_insert'),
    url(r'^(?P<pk>[0-9]+)/detail/$', views.board_detail.as_view(), name='board_detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.board_update.as_view(), name='board_update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.board_delete.as_view(), name='board_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)