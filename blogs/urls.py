from django.urls import path
from . import views


urlpatterns = [
    path("",views.Index.as_view(),name="index-page"),
    path("post/",views.AllPosts.as_view(),name="post-page"),
    path("post/<slug:slug>",views.PostDetail.as_view(),name="post-detail-page"),
]
