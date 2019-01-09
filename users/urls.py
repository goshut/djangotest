from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^index/$', views.index),
    # url(r'^say/$', views.say),
    url(r'^hand/(?P<b>\d{3})/(?P<a>[A-z]{3})/$', views.hand),
]