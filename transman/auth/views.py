from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import auth

# Create your views here.
def home(request):
    if request.user.is_authenticated():
        group=request.user.groups.all()[0].name
        if group=='a':
            return redirect('/work/list')
        if group=='b':
            return redirect('/work/b')
        if group=='c':
            return redirect('/work/c')
    return render(request,'auth/login.html',{})

def logout(request):
    if request.user.is_authenticated():
        auth.logout(request)
    return redirect('/')

def login(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    if not username or not password:
        return HttpResponse('input error')
    user=auth.authenticate(username=username,password=password)
    if user is None:
        return HttpResponse('username or password wrong')
    auth.login(request,user)
    return redirect('/')
