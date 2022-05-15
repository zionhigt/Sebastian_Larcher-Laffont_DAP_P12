from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from customer.serializers import CustomerListSerializer, CustomerUpdateSerializer, CustomerDetailSerializer
from customer.permissions import IsAuthorOrReadOnly


class CustomerViewSet(ModelViewSet):
    list_serializer_class = CustomerListSerializer
    detail_serializer_class = CustomerDetailSerializer
    update_serializer_class = CustomerUpdateSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly, ]

    def get_queryset(self):
        pass

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return self.update_serializer_class
        if self.action in ['list']:
            return self.list_serializer_class
        if self.action in ['retrieve', 'create']:
            return self.detail_serializer_class

        return super().get_serializer_class()

