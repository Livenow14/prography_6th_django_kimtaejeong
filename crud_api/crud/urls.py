"""from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
app_name = 'crud'

router = routers.DefaultRouter()
router.register('Hi', views.Crud)
urlpatterns = [
    url('api-auth/', include('rest_framework.urls')),
    url(r'^$', include(router.urls)),

    #url('list', views.Todo_subject_restful_main.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)"""