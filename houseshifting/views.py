from django.http import HttpResponse
from django.shortcuts import render

# def Contact(request):
#             return render(request,"contact.html")

def Contact(request):
    return render(request,"contact.html")




def Index(request):
    return render(request,"index.html")

def Qoute(request):
    return render(request,"qoute.html")

def About(request):
    return render(request,"about.html")


def Blog(request):
    return render(request,"blog.html")

def Service(request):
    return render(request,"service.html")

def Base(request):
    return render(request,"base.html")



def New(request):
    return render(request,"new.html")