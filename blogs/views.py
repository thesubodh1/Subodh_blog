from typing import Any
from django.shortcuts import render
from datetime import date
from .models import Post
from django.views.generic import ListView,DetailView
from django.views import View
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse




# def get_date(post):
#     return post['date']


# converting index view into list view
# def index(request):
#     leatest_post = Post.objects.all().order_by('-date')[:3]
#     return render(request,"blogs/index.html",{
#         "posts" : leatest_post,
#     })

class Index(ListView):
    template_name = "blogs/index.html"
    model = Post
    context_object_name = "posts"
    ordering = ["-date"]

    def get_queryset(self):
        query_set = super().get_queryset()
        leatest_posts = query_set[:3]
        return leatest_posts
  
    

# converting posts view into listview
# def posts(request):
#     all_posts = Post.objects.all()
#     return render(request,"blogs/all-post.html",{
#         "all_posts" : all_posts,
#     })
class AllPosts(ListView):
    template_name = "blogs/all-post.html"
    model = Post
    context_object_name = "all_posts"
    ordering = ["date"]

# #converting Post view into listview
# def post(request,slug):
#     post = Post.objects.get(slug=slug)
#     return render(request,"blogs/post-detail.html",{
#         "one_post" : post,
#         "post_tags" : post.tag.all()
#     })

class PostDetail(DetailView):
    template_name = "blogs/post-detail.html"
    model = Post
    context_object_name = "one_post"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        post = self.object
        context["post_tags"] = post.tag.all()
        return context
    

class PostDetail(View):
    def get(self,request,slug):
        post = Post.objects.get(slug=slug)
        context = {
            "one_post" : post,
            "post_tags" : post.tag.all(),
            "form" : CommentForm,
            "comments" : post.comment.all()
        }
        return render(request,"blogs/post-detail.html",context)

    def post(self,request,slug):
        post = Post.objects.get(slug = slug)
        form = CommentForm(request.POST)

        if form.is_valid():
           comment =  form.save(commit=False)
           comment.post = post
           comment.save()
           return HttpResponseRedirect(reverse("post-detail-page",args=[slug]))
        
        context = {
            "one_post" : post,
            "post_tags"  :post.tag.all(),
            "form" : form,
            "comments" : post.comment.all()
        }
        return render(request,"blogs/post-detail.html",context)
    

class ReadLater(View):
    pass