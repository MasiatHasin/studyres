from django.urls import path

from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.index, name="index"),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('post/', views.saveResource, name='post'),
    path("confirmation/", views.confirmation, name="confirmation"),
    path('query/', views.queryResource, name="query"),
]