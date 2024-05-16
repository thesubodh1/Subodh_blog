from django.shortcuts import render

def index(request):
    return render(request,"blogs/index.html")

def posts(request):
    return render(request,"blogs/all-post.html")

def post(request,slug):
    return render(request,"blogs/post-detail.html")