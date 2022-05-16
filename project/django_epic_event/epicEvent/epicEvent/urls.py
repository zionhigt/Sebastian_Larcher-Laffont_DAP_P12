"""epicEvent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentication.views import RegisterViewSet

from customer.views import CustomerViewSet
from contrat.views import ContratViewSet
from event.views import EventViewSet

customers_url_paterns = [
    path('api/customer/', CustomerViewSet.as_view({"get": "list"}), name='list_customers'),
    path('api/customer/<int:pk>/', CustomerViewSet.as_view({"get": "retrieve"}), name='list_customers'),
    path('api/customer/create/', CustomerViewSet.as_view({"post": "create"}), name='create_customer'),
    path('api/customer/update/<int:pk>/', CustomerViewSet.as_view({"put": "update"}), name='update_customer'),
    path('api/customer/delete/<int:pk>/', CustomerViewSet.as_view({"delete": "delete"}), name='delete_customer'),
]

events_url_paterns = [
    path('api/event/', EventViewSet.as_view({"get": "list"}), name='list_events'),
    path('api/event/<int:pk>/', EventViewSet.as_view({"get": "retrieve"}), name='list_events'),
    path('api/event/create/', EventViewSet.as_view({"post": "create"}), name='create_event'),
    path('api/event/update/<int:pk>/', EventViewSet.as_view({"put": "update"}), name='update_event'),
    path('api/event/delete/<int:pk>/', EventViewSet.as_view({"delete": "delete"}), name='delete_event'),
]

contrats_url_paterns = [
    path('api/contrat/', ContratViewSet.as_view({"get": "list"}), name='list_contrats'),
    path('api/contrat/<int:pk>/', ContratViewSet.as_view({"get": "retrieve"}), name='list_contrats'),
    path('api/contrat/create/', ContratViewSet.as_view({"post": "create"}), name='create_contrat'),
    path('api/contrat/update/<int:pk>/', ContratViewSet.as_view({"put": "update"}), name='update_contrat'),
    path('api/contrat/delete/<int:pk>/', ContratViewSet.as_view({"delete": "delete"}), name='delete_contrat'),
    path('api/contrat/sign/<int:pk>/', ContratViewSet.as_view({"patch": "sign"}), name='sign_contrat'),
]

urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/create/', RegisterViewSet.as_view({"get": "list"}), name='signup'),
    path('admin/', admin.site.urls)
] + customers_url_paterns + events_url_paterns + contrats_url_paterns
