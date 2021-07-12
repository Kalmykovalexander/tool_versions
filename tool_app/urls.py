from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'tool_app'
urlpatterns = [
    # create object
    path('tool/create/', ToolCreateView.as_view()),
    # display all objects
    path('all/', ToolsListView.as_view()),
    # retrieve, update, delete object
    path('tool/detail/<int:pk>/', ToolDetailView.as_view()),
]