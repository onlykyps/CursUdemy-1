from django.contrib import admin
from django.urls import path


from .views import (
        post_list,
        post_create,
        post_home,
        post_detail,
        post_update,
        post_delete,
    )

# from posts import views

urlpatterns = [
    # path('posts/', views.post_home),
    path('posts/', post_home),
    path('create/', post_create),
    path('/(P<id>\d+)/', post_detail, name="post_detail"),
    path('',post_list),
    path('updat/', post_update),
    path('delete/', post_delete),
]
