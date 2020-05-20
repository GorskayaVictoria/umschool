import smtplib
import uuid
#
from django.http import HttpResponse, HttpResponseRedirect

# from user.service import send_email
from app_celery.celery import send_email
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import render, redirect

# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.utils.encoding import force_text, force_bytes


import user
from task.models import Task1
from umschool import settings
from user.forms import LoginForm, RegForm, EditForm, ForgotForm, EmailForm
from user.models import User, UserToken


@login_required(login_url=reverse_lazy('login'))
def profile_view(request):
    user = request.user
    print(User.objects.get(id=user.id).profile_pic)
    return render(request, "profile.html", {"user": user,"lessons":user.lesson_set.all()})


def login_view(request):
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                user = authenticate(
                    username=form.cleaned_data["username"],
                    password=form.cleaned_data["password"])
                print(user)
                if user is not None:
                    login(request, user)
                    return redirect(reverse("index"))
                else:
                    return render(request, "login.html", {"form": form, "errors": ["Incorrect login or password"]})
            else:

                return render(request, "login.html", {"form": form})
        else:
            form = LoginForm()
            return render(request, "login.html", {"form": form})


@login_required(login_url="/auth/login")
def logout_view(request):
    logout(request)
    return redirect(reverse("login"))


def registration(request):
        if request.method == "POST":
            form = RegForm(request.POST,request.FILES)
            if form.is_valid():
                if form.cleaned_data["password"]!= form.cleaned_data["confirm_password"]:
                    return render(request, "register.html", {"form": form, "errors": ["Incorrect confirmpassword"]})
                else:
                    user = User.objects.create_user(
                    username=form.cleaned_data["username"],
                    email=form.cleaned_data["email"],
                    password=form.cleaned_data["password"],
                    first_name=form.cleaned_data["first_name"],
                    last_name=form.cleaned_data["last_name"])
                    user.profile_pic = form.cleaned_data["profile_pic"]
                user = authenticate(
                    username=form.cleaned_data["username"],
                    password=form.cleaned_data["password"])
                login(request, user)
                return redirect(reverse("index"))
            else:
                return render(request, "register.html", {"form": form})
        else:
            return render(request, "register.html", {"form": RegForm()})



def index(request):
    print(User.__dict__)
    # print(hello())
    return render(
        request, 'index.html',
        context={})

def delall(request):
    task = Task1.objects.all()
    for task1 in task:
        print(task1.thema)
        task1.save()

    return render(
        request, 'index.html',
        context={})

@login_required(login_url="/auth/login")
def edit(request):
    if request.method == "POST":
        form = EditForm(request.POST,request.FILES)
        if form.is_valid():
            username = form.cleaned_data["username"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            profile_pic = form.cleaned_data["profile_pic"]
            email = form.cleaned_data["email"]
            if username != "":
                request.user.username = username
                request.user.save()
            if first_name != "":
                request.user.email = first_name
                request.user.save()
            if last_name != "":
                request.user.email = last_name
                request.user.save()
            if profile_pic != "":
                request.user.profile_pic = profile_pic
                request.user.save()
            if email != "":
                request.user.email = email
                request.user.save()
            user = authenticate(
                username=request.user.username,
                password=request.user.password)
            login(request, user)
            return redirect(reverse("index"))
        else:
            return render(request, "edit.html", {"form": form})
    else:
        return render(request, "edit.html", {"form": EditForm()})

def resetNone(request):
    if request.user.is_authenticated:
        return redirect(reverse("editPass"))
    if request.method == "GET":
        form = EmailForm()
        return render(request, "email.html", {"form": form,})
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            print(request.user)

            user = User.objects.get(email=form.cleaned_data['email'])
            token = default_token_generator.make_token(user)
            UserToken.objects.create(token=token,user=user)
            send_email.delay("сброс", settings.DEFAULT_FROM_EMAIL, user.email,
                       'mail.html', args=dict(name=user.username, token=token))
            return HttpResponse()

def editPass(request):
    if not request.user.is_authenticated:
        return redirect(reverse("resetNone"))
    token = default_token_generator.make_token(request.user)
    UserToken.objects.create(token=token, user=request.user)
    send_email.delay("сброс", settings.DEFAULT_FROM_EMAIL, request.user.email,'mail.html', args=dict(name=request.user.username, token=token))
    return HttpResponse()

def reset_password(request,token):
    if not UserToken.objects.filter(token=token):
        return redirect(reverse("index"))
    else:
        if request.method == "GET":
            form = ForgotForm()
            return render(request, "forgot.html", {"form": form, "token":token})
        elif request.method == "POST":
            form = ForgotForm(request.POST)
            if form.is_valid():
                passw = form.cleaned_data["password"]
                passw2 = form.cleaned_data["confirm_password"]
                if (passw==passw2):
                    user = UserToken.objects.get(token=token).user
                    user.set_password(passw)
                    user.save()
                    user2 = authenticate(
                        username=user.username,
                        password=passw)
                    login(request, user2)
                    return redirect(reverse("index"))





