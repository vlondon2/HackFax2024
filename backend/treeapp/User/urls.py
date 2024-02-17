from django.urls import path

from . import views

urlpatterns = [
    path("create", views.createUser, name="createUser"),
    path("get", views.getUser, name="getUser"),
    path("completeTask", views.completeTask, name="completeTask"),
    path("createDev", views.createDevUser, name="createDevUser"),
    path("buy", views.buyCosmetic, name="buyCosmetic")
]