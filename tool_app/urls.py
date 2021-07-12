from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'tool_app'
urlpatterns = [
    path('tool/create/', ToolCreateView.as_view()),
    path('all/', ToolsListView.as_view()),
    path('tool/detail/<int:pk>/', ToolDetailView.as_view()),
]