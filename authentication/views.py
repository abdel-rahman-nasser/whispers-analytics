from django.shortcuts import render

# Create your views here.
from aiohttp import request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from social_media_monitoring.models import social_Data

class authentication:

    def sign_up(request):
        if request.user.is_authenticated:
            return redirect("sections")
        if request.method=="POST":
            username=request.POST.get("username")
            email=request.POST.get("email")
            password=request.POST.get("password")
            fc_url=request.POST.get("face")
            insta1=request.POST.get("insta")
            twt=request.POST.get("twitter")
            if User.objects.filter(username=username):
                messages.error(request, "Username already exists! Please try some other username.")
                return redirect('register')

            if User.objects.filter(email=email).exists():
                messages.error(request, "Email Already Registered!!")
                return redirect('register')

            if social_Data.objects.filter(face_url=fc_url).exists():
                messages.error(request, "Face book URL Already exists!!")
                return redirect('register')

            if social_Data.objects.filter(twitter=twt).exists():
                messages.error(request, "Twitter User Already exists!!")
                return redirect('register')

            if social_Data.objects.filter(insta=insta1).exists():
                messages.error(request, "Instagram User Already exists!!")
                return redirect('register')
            
            if len(username)>20:
                messages.error(request, "Username must be under 20 charcters!!")
                return redirect('register')

            user=User.objects.create_user(username,email,password)
            user.username=username
            user.save()
            user_social_info=social_Data(s_user=username,face_url=fc_url,insta=insta1,twitter=twt)
            user_social_info.save()
            messages.success(request,"Ur Account has been successfully Created")

            return redirect("login")
        return render(request, "authentication/register.html")

    def welcome(request):
        return render(request, "authentication/welcome.html")

    def sign_in(request):
        if request.user.is_authenticated:
            return redirect("sections")
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("sections")

            else:
                messages.error(request, "Bad Credentials")
                return redirect("login")

        return render(request, "authentication/login.html")

    def sign_out(request):
        if request.user.is_authenticated:
            logout(request)
            return redirect("welcome")
        else:
            return redirect("login")
