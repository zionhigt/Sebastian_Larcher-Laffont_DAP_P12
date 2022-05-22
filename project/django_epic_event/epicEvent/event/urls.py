from django.urls import path

from event.views import EventViewSet


events_url_paterns = [
    path('api/event/', EventViewSet.as_view({"get": "list"}), name='list_events'),
    path('api/event/<int:pk>/', EventViewSet.as_view({"get": "retrieve"}), name='list_events'),
    path('api/event/create/', EventViewSet.as_view({"post": "create"}), name='create_event'),
    path('api/event/update/<int:pk>/', EventViewSet.as_view({"put": "update"}), name='update_event'),
    path('api/event/delete/<int:pk>/', EventViewSet.as_view({"delete": "delete"}), name='delete_event'),
]