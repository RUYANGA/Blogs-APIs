from django.urls import path
from . import views
urlpatterns = [
    path("",views.index),
    path('getposts/',views.getAllPosts),
    path("create/",views.createPost)
]
