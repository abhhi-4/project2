from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fnsample(request):
    return HttpResponse ("abhishek")
def fn1(request):
    return render(request,'abhishek.html')
def fn2(request):
    return render(request,'login.html')