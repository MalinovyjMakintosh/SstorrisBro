from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', views.registration_view, name='registration'),
    path('auth/', include('social_django.urls', namespace='social')),
]
