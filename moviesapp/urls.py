from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.movies_list, name='movies_list'),
]
