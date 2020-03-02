from django.conf.urls import url, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'board'

urlpatterns = [
    url(r'^$', views.board.as_view(), name='board'),
    url(r'^insert/$', views.check_post, name='board_insert'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)