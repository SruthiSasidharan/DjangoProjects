from django.contrib import admin
from django.urls import path
from .views import ReviewCreateView

urlpatterns = [
   path("rev",ReviewCreateView.as_view(),name="rev")

]
