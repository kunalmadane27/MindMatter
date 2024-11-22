from django.urls import path, include
from .views import *

urlpatterns = [
    path("", CreateAndGetAllBlogs.as_view()),
    path("/<int:pk>", GetUpdateDeleteBlogs.as_view())]
