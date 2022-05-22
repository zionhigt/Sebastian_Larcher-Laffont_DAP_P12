from django.urls import path
from django.contrib import admin

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentication.views import RegisterViewSet


authentication_url_paterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/create/', RegisterViewSet.as_view({"get": "list"}), name='signup'),
    path('admin/', admin.site.urls)
]