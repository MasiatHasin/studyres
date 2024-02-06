from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_view, name="index"),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('post/', views.saveResource, name='post'),
    path("confirmation/", views.confirmation, name="confirmation"),
]