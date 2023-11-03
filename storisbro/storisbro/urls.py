from django.urls import path, include
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Your API",
      default_version='v1',
      description="Your description here",
      terms_of_service="https://www.yourapp.com/terms/",
      contact=openapi.Contact(email="contact@yourapp.com"),
      license=openapi.License(name="Your License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
   path('api/vk-login/', include('social_django.urls', namespace='social')),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   # Your other API endpoints
]


urlpatterns = [
    path('register/', views.UserRegistration.as_view(), name='user-registration'),
    path('verify-code/', views.VerifyCode.as_view(), name='verify-code'),
    path('api/', include('appname.urls')),
]
