from django.shortcuts import render
from datetime import date
from .models import Post


def get_date(post):
    return post['date']



def index(request):
    leatest_post = Post.objects.all().order_by('-date')[:3]
    return render(request,"blogs/index.html",{
        "posts" : leatest_post,
    })

def posts(request):
    all_posts = Post.objects.all()
    return render(request,"blogs/all-post.html",{
        "all_posts" : all_posts,
    })

def post(request,slug):
    post = Post.objects.get(slug=slug)
    return render(request,"blogs/post-detail.html",{
        "one_post" : post,
        "post_tags" : post.tag.all()
    })