from django.urls import path

from contrat.views import ContratViewSet


contrats_url_paterns = [
    path('api/contrat/', ContratViewSet.as_view({"get": "list"}), name='list_contrats'),
    path('api/contrat/<int:pk>/', ContratViewSet.as_view({"get": "retrieve"}), name='list_contrats'),
    path('api/contrat/create/', ContratViewSet.as_view({"post": "create"}), name='create_contrat'),
    path('api/contrat/update/<int:pk>/', ContratViewSet.as_view({"put": "update"}), name='update_contrat'),
    path('api/contrat/delete/<int:pk>/', ContratViewSet.as_view({"delete": "delete"}), name='delete_contrat'),
    path('api/contrat/sign/<int:pk>/', ContratViewSet.as_view({"patch": "sign"}), name='sign_contrat'),
]