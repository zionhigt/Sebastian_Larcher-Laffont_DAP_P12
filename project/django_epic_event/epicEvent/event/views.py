from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from event.serializers import EventListSerializer, EventUpdateSerializer, EventDetailSerializer
from event.permissions import IsAuthorOrReadOnly


class EventViewSet(ModelViewSet):
    list_serializer_class = EventListSerializer
    detail_serializer_class = EventDetailSerializer
    update_serializer_class = EventUpdateSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly, ]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'contrat_id__customer_id__name',
        'contrat_id__customer_id__email',
        'contrat_id__date_created',
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

        return super().get_serializer_class()

