from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from .forms import *

# Creating redirection page
def main(request):
    return render(request, 'main.html', {})

# Faculty Login
def faculty_login(request):
    print(request.user.is_authenticated())
    title = "Faculty Login"
    form = FacultyLoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(email=email, password=password)
        login(request, user)
        print(request.user.is_authenticated())
    return render(request, "registration/facultylogin.html", {"form":form, "title":title})

def hod_login(request):
    print(request.user.is_authenticated())
    title = "Department Head Login"
    form = HODLoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(email=email, password=password)
        login(request, user)
        print(request.user.is_authenticated())
    return render(request, "registration/hodlogin.html", {"form":form, "title":title})


# Post-Faculty Login
def findex(request):
    return render(request, 'faculty/findex.html', {})


