from django.urls import path

from . import views

urlpatterns = [
    path('', views.master, name='master'),
    path('detail', views.detail, name='detail'),
]
