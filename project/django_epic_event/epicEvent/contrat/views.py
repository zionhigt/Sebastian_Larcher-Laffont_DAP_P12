from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from contrat.serializers import (
    ContratListSerializer,
    ContratUpdateSerializer,
    ContratDetailSerializer,
    ContratSignSerializer
)
from contrat.permissions import IsAuthorOrReadOnly
from contrat.models import Contrat

class ContratViewSet(ModelViewSet):
    list_serializer_class = ContratListSerializer
    detail_serializer_class = ContratDetailSerializer
    update_serializer_class = ContratUpdateSerializer
    sign_serializer_class = ContratSignSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly, ]

    filterset_customfields = {
        "customer_firstname": 'customer_id__first_name',
        "customer_lastname": 'customer_id__last_name',
        "customer_email": 'customer_id__email',
        "date_created": 'date_created',
        "date_created__lt": 'date_created__lt',
        "date_created__gt": 'date_created__gt',
        "amount": 'amount',
        "amount__lt": 'amount__lt',
        "amount__gt": 'amount__gt',
    }

    def parse_params(self, params):
        params = dict(params)
        new_params = {}
        for param, value in params.items():
            param = self.filterset_customfields.get(param, None)
            if param is not None:
                if type(value) is list:
                    if len(value) > 1:
                        param += "__in"
                    if len(value) == 1:
                        value = value[0]
                    
                new_params[param] = value
        return new_params

    def get_queryset(self):
        filter_ids = []
        filters = self.parse_params(self.request.query_params)
        all_records = Contrat.objects.all()
        if len(filters.items()):
            all_records = all_records.filter(**filters)
        filter_ids = [int(record.id) for record in all_records]
        if self.request.user.role.name != "MANAGER":
            filter_ids = [int(record.id) for record in all_records if record.salesman_id.id == self.request.user.id]
        return all_records.filter(id__in=filter_ids)

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
