from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
# Create your views here.

@api_view(['GET'])
def index(request):
    return Response({"Success":"The setup was successful"})

@api_view(['GET'])
def getAllPosts(request):
   get_post=Post.objects.all()
   return Response(get_post)