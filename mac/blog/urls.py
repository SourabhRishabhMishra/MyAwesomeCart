

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("blogpost/", views.blogpost, name="blogpost")
]

