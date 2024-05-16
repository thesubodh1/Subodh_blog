from django.urls import path
from . import views


urlpatterns = [
    path("",views.index,name="index-page"),
    path("post/",views.posts,name="post-page"),
    path("post/<slug:slug>",views.post,name="post-detail-page"),
]
