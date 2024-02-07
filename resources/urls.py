from django.urls import path


from . import views

urlpatterns = [
    path("", views.home_view, name="index"),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('post/', views.saveResource, name='post'),
    path('upvote/<int:id>', views.upvote, name="upvote"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('resource/<int:id>', views.resource_view, name="resource"),
    path("confirmation/", views.confirmation, name="confirmation"),
]