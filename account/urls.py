from django.conf.urls import url
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^login/$', views.user_login, name='user_login'),
]