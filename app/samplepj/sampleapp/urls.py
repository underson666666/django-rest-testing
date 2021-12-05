from django.contrib import admin
from django.urls import path
from . import views
from .rest.User import User

urlpatterns = [
    path(
        'user',
        User.as_view(),
        name='user'
        ),
    ]
