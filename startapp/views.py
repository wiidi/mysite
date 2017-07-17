from django.shortcuts import render
from django.shortcuts import HttpResponse
from startapp import models

user_list=[
    {'user':"wudi","pwd":"wiod"}
]
def index(request):
    if request.method=="POST":
        username=request.POST.get("username",None)
        password=request.POST.get("password",None)
        print (username,password)
        tmp={"user":username,"pwd":password}
        models.UserInfo.objects.create(user=username,pwd=password)
        #return render(request,"first.html",{"data":user_list})
    user_list=models.UserInfo.objects.all()

    return render(request,"index.html",{"data":user_list})
    #return  HttpResponse("hello world !!!")
