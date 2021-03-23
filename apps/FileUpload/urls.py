from django.urls import path, include
from . import views

urlpatterns = [
    # file upload links
    path('', views.dashboard),
    path('dashboard', views.dashboard),
    path('upload', views.fileupload, name="file_upload"),

    # login & register naviagation
    path('ln/', include('apps.Login_Register.urls')),
]