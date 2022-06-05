from django.urls import path

from customer.views import CustomerViewSet


customers_url_paterns = [
    path('api/customer/', CustomerViewSet.as_view({"get": "list"}), name='list_customers'),
    path('api/customer/<int:pk>/', CustomerViewSet.as_view({"get": "retrieve"}), name='list_customers'),
    path('api/customer/create/', CustomerViewSet.as_view({"post": "create"}), name='create_customer'),
    path('api/customer/update/<int:pk>/', CustomerViewSet.as_view({"put": "update"}), name='update_customer'),
    path('api/customer/delete/<int:pk>/', CustomerViewSet.as_view({"delete": "delete"}), name='delete_customer'),
]
