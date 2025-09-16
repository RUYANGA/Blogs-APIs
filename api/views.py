from django.shortcuts import render
from rest_framework.decorator import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def index(request):
    return Response({"Success":"The setup was successful"})