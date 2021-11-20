from django.contrib import admin
from django.urls import path, include
from .endpoint import views
urlpatterns = [
    path('',views.index)
]