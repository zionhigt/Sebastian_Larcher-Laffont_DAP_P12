from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from contrat.serializers import (
    ContratListSerializer,
    ContratUpdateSerializer,
    ContratDetailSerializer,
    ContratSignSerializer
)
from contrat.permissions import IsAuthorOrReadOnly


class ContratViewSet(ModelViewSet):
    list_serializer_class = ContratListSerializer
    detail_serializer_class = ContratDetailSerializer
    update_serializer_class = ContratUpdateSerializer
    sign_serializer_class = ContratSignSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly, ]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'customer_id__name',
        'customer_id__email',
        'date_created', 'amount'
    ]

    # def get_queryset(self):
    #     pass

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return self.update_serializer_class
        if self.action in ['list']:
            return self.list_serializer_class
        if self.action in ['retrieve', 'create']:
            return self.detail_serializer_class
        if self.action in ['sign']:
            return self.sign_serializer_class

        return super().get_serializer_class()

