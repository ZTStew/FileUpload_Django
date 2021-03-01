from django.urls import path, include
from . import views

urlpatterns = [
    # default link
    path('', views.default),

    path('login', views.login),
    path('register', views.register),
    path('logout', views.logout),
]
