from django.conf.urls import url,include
from django.contrib import admin
from rest_framework import routers
from movies.views import MovieViewSet

router = routers.DefaultRouter()
router.register('movies',MovieViewSet) # prefix = movies , viewset = MovieViewSet

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include(router.urls)),
]