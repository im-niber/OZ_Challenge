from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/schema', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger_ui'),
    path('api/v1/schema/redoc/', SpectacularSwaggerView.as_view(url_name='schema'), name='redoc'),
    path('api/v1/videos/', include('videos.urls')),
    path('api/v1/subscriptions/', include('subscriptions.urls')),
]
