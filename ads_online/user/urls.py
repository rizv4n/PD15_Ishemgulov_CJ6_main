from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user.views import Logout, UserUploadView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='access_token'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('logout/', Logout.as_view(), name='user_logout'),
    path('<int:pk>/upload/', UserUploadView.as_view(), name='upload_image')
]
