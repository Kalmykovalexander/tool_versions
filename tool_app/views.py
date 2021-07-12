from django.shortcuts import render
from rest_framework import generics

from .models import Tool
from .serializers import *


# View for Create objects
class ToolCreateView(generics.CreateAPIView):
    serializer_class = ToolDetailSerializer

# View for display all objects
class ToolsListView(generics.ListAPIView):
    serializer_class = ToolListSerializer
    queryset = Tool.objects.all()


# View for retrieve, update, delete object
class ToolDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ToolDetailSerializer
    queryset = Tool.objects.all()
