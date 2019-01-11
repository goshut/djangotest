from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^redis_store/$', views.redis_store),
]
