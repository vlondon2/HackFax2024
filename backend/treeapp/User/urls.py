from django.urls import path

from . import views

urlpatterns = [
    path("create", views.createUser, name="createUser"),
    path("get", views.getUser, name="getUser")
]