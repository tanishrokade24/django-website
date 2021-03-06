from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('blogpage', views.blogpage, name='blogpage'),
    path('travel_blog', views.travel_blog, name='travel'),
    #path('travel_blog_submit', views.travel_blog_submit, name='travel'),
]
