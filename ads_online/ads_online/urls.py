from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter

from user import urls as user_urls
from ads.urls import ad as ad_urls

users_router = SimpleRouter()
users_router.register("users", UserViewSet, basename="user")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(users_router.urls)),
    path('api/', include(user_urls)),
    path('api/ads/', include(ad_urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
]
