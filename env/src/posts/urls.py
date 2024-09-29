from django.contrib import admin
from django.urls import path

from . import views

# from posts import views

urlpatterns = [
    
    # path('posts/', views.post_home),
    path('posts/', "posts.views.post_home"),
    path('create/', "posts.views.post_create"),
    path('detail/', "posts.views.post_detail"),
    path('list/', "posts.views.post_list"),
    path('updat/', "posts.views.post_update"),
    path('delete/', "posts.views.post_delete"),
]
