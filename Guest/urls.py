from django.contrib import admin
from django.urls import path
from .views import RegistrationView,LoginView,CreateLibrary,ListLibrary,UpdateLibrary,Deletelibrary,UpdateReview
urlpatterns = [
    path("reg",RegistrationView.as_view(),name="reg"),
    path("log",LoginView.as_view(),name="log"),
    path("create",CreateLibrary.as_view(),name="create"),
    path("list",ListLibrary.as_view(),name="list"),
    path("edit/<int:pk>",UpdateLibrary.as_view(),name="edit"),
    path("delete/<int:pk>",Deletelibrary.as_view(),name="delete"),
    path("rev",UpdateReview.as_view(),name="rev")
]
