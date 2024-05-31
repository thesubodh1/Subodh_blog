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
    def is_stored_post(self,request,post_id):
        stored_post = request.session.get("stored_posts")
        if stored_post is not None:
            is_saved_for_later = post_id in stored_post
            print(is_saved_for_later)
        else:
            is_saved_for_later = False

        return is_saved_for_later
    
    def get(self,request,slug):
        post = Post.objects.get(slug=slug)
        context = {
            "one_post" : post,
            "post_tags" : post.tag.all(),
            "form" : CommentForm,
            "comments" : post.comment.all().order_by('-id'),
            "is_saved" : self.is_stored_post(request,post.id)
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
            "comments" : post.comment.all().order_by('-id'),
            "is_saved" : self.is_stored_post(self,post.id)
        }
        return render(request,"blogs/post-detail.html",context)
    

class ReadLater(View):
  def post(self,request):
      stored_post = request.session.get("stored_posts")

      if stored_post is None:
          stored_post = []

      post_id = int(request.POST["post-id"])
      if post_id not in stored_post:
        stored_post.append(post_id)
      else:
        stored_post.remove(post_id)
      request.session["stored_posts"] = stored_post
      return HttpResponseRedirect("/")
  

  def get(self,request):
      stored_post = request.session.get("stored_posts")

      context = {}

      if stored_post is None or len(stored_post) == 0:
           context["posts"] = []
           context["has_posts"] = False
      else:
          post = Post.objects.filter(id__in = stored_post)
          context["posts"] = post
          context["has_posts"] = True
      return render(request,"blogs/read-later.html",context)

     


