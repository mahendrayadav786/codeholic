from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.home, name='home'),
    path("contact/", views.contact, name='home'),
    path("about/", views.about, name='home'),
    path("search/", views.search, name='search'),
    path("signup/", views.handleSignup, name='handleSignup'),
    path("login/", views.handlelogin, name="handlelogin"),
    path("logout/", views.handlelogout, name='handlelogout'),
    path("projects/",views.projects, name="projects")


]