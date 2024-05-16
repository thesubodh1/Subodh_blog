from django.shortcuts import render

def index(request):
    return render(request,"blogs/index.html")

def posts(request):
    pass

def post(request):
    pass