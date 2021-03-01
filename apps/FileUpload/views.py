from django.shortcuts import render, redirect
from apps.Login_Register.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return(render(request, "FileUpload/dashboard.html"))

def dashboard(request):
    # if "user_id" not in request.session:
        # return(redirect("/ln"))
    return render(request, "FileUpload/dashboard.html")
