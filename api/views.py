from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
# Create your views here.

@api_view(['GET'])
def index(request):
    return Response({"Success":"The setup was successful"})

@api_view(['GET'])
def getAllPosts(request):
   get_posts=Post.objects.all()
   serialezer=PostSerializer(get_posts,many=True)
   
   return Response(serialezer.data)

@api_view(['GET','POST'])
def createPost(request):
    data=request.data
    serializer= PostSerializer(data=data)
    
    if serializer.is_valid():
        serializer.save()
        return Response({"success":"POst created successful"},status=201)
    else:
        return Response(serializer.errors,status=400)
    
@api_view(['DELETE'])
def deletePost(request):
    postId=request.data.get('id')
    try:
        post=Post.objects.get(id=postId)
        post.delete()
        
        return Response({'success':"Post deleted successful"})
    except Post.DoesNotExist:
        return Response({"Error":"The post does not exist"},status=404)
    
@api_view(['GET'])
def getOne(request):
    id=request.data.get('id')
    try:
        post=Post.objects.get(id=id)
        serielizer=PostSerializer(post)
        return Response(serielizer.data)
    except Post.DoesNotExist:
        return Response({"Error":"The post does not exist"},status=404)
        
@api_view(['PUT'])
def updatePost(request):
    id=request.data.get('id')
    new_title=request.data.get('title')
    new_content=request.data.get('content')
    
    try:
        post=Post.objects.get(id=id)
        
        if new_title:
            post.title=new_title
        if new_content:
            post.content=new_content
        post.save()
        
        return Response({"success":"Post updated successful"})        
    except Post.DoesNotExist:
        return Response({"Error":"The post does not exist"},status=404)