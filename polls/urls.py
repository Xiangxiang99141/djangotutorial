from django.urls import path
from . import views

#定義路由應射到程式
urlpatterns = [
    path("", views.index, name="index"),
]