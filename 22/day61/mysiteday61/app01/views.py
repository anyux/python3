from django.shortcuts import HttpResponse,render,redirect
from app01 import models

def index(request):
    return render(request,"index.html")

def weibo(request):
    return HttpResponse("叶小钗")

def login(request):
    print("运行的是app01的应用")
    error_msg = ""
    if request.method == "POST":
        email = request.POST.get('email',None)
        pwd = request.POST.get('pwd',None)
        if email == "1@1" and pwd == "1":
            return redirect("http://www.baidu.com/s?wd=素还真")
        else:
            error_msg = "邮箱或密码错误"
    return render(request,"login.html",{"error_msg":error_msg})

def user_list(request):
    user_list = models.UserInfo.objects.all()
    return render(request,"user_list.html",{"user_list":user_list})

def user_add(request):
    if request.method == "POST":
        user = request.POST.get('user')
        models.UserInfo.objects.create(name=user)
        return redirect("/user_list/")
    else:
        return render(request,"user_add.html")
