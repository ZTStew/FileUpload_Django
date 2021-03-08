from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# catch-all
def default(request):
    # sends user to dash if they are already logged in
    if "user_id" in request.session:
        print("ERROR <default>: user logged in already")
        return(redirect("/dashboard"))

    # prints all user emails to server console (to make logging in easier)
    userList = User.objects.all()
    for i in userList:
        print("Email: " + i.email);

    # sends user to login page
    return render(request, "Login_Register/login_register.html")

def register(request):
    results = User.objects.validate(request.POST)
    if not results[0]:
        for error_message in results[1]:
            messages.add_message(request, messages.ERROR, error_message)
    else:
        messages.add_message(request, messages.SUCCESS, 'You are Now Registered.', fail_silently = True)

    return(redirect("./"))

def login(request):
    results = User.objects.log(request.POST)
    # print(results[1].user_name)

    if not results[0]:
        for error_message in results[1]:
            messages.add_message(request, messages.ERROR, error_message)
        return(redirect("./"))
    else:
        request.session["user_id"] = results[1].id
        print("NOTICE <login>: user, \"" + results[1].user_name + "\" is now logged in.")
        return(redirect("/dashboard"))

def logout(request):
    # entries = User.objects.all()
    # # entries = User.objects(user_id="1")
    # print(entries)
    # print(entries[1].user_name)
    # print("#####################")

    # obj = User.objects.get(pk=request.session["user_id"])
    # print(obj.user_name)

    # print(User.objects.get(pk=request.session["user_id"]).user_name)

    # prints out the 'user_name' of the person that has logged out
    print("NOTICE <logout>: user, \"" + User.objects.get(pk=request.session["user_id"]).user_name + "\" has logged out.")
    request.session.clear()
    return redirect("./")

# def users_api(request):
#     users = User.objects.filter(first_name__startswith=request.POST['starts_with'])
#     return render(request, 'Login_Register/login_register.html', { users: users })
