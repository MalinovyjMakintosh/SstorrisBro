from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.user_profile, name='user-profile'),
    path('create/', views.create_item, name='create-item'),
]
