from django.conf.urls import url
from . import views


urlpatterns = [
    url('^classview/$', views.View1.as_view())
]