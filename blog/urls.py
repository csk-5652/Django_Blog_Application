from django.contrib import admin
from django.urls import path
from blog import views  

urlpatterns = [
    path("",views.index,name="index"),
    path("blog",views.blog,name="blog"),
    path('blogpost/<str:slug>',views.blogpost,name="blogpost"),
    path('search',views.search,name="search"),
    path('profile',views.profile,name="profile"),
    
    
]
