from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
#from rest_framework import routers
app_name = 'crud'

#router = routers.DefaultRouter()
#router.register(r'todfo', views.Todo_subject_restful_main)
urlpatterns = [
  #  url('api-auth/', include('rest_framework.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')), # Login, Logout 관련 기능
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')), # SignUp 관련 기능
    url(r'^$', views.Crud.as_view(), name='crud'),
    url(r'^crud_list/$', views.Crud_list.as_view(), name='crud_list'),
    url(r'^crud_list/create/$', views.Crud_create.as_view(), name='crud_create'),
    url(r'^crud_list/(?P<id>\d+)/$', views.Crud_detail.as_view(), name='crud_detail'),
    url(r'^crud_list/(?P<id>\d+)/update/$', views.Crud_update.as_view(), name='crud_update'),
    url(r'^crud_list/(?P<id>\d+)/delete/$', views.Crud_delete.as_view(), name='crud_delete'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, insecure=True)
