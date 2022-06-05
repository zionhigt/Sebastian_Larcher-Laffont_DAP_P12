from rest_framework.serializers import ModelSerializer
from contrat.models import Contrat


class ContratListSerializer(ModelSerializer):

    class Meta:
        model = Contrat
        fields = ['id', "customer_id", "salesman_id", "amount"]


class ContratUpdateSerializer(ModelSerializer):

    class Meta:
        model = Contrat
        fields = [
            "salesman_id",
            "status",
            "amount",
            "payment_due",
        ]


class ContratDetailSerializer(ModelSerializer):

    class Meta:
        model = Contrat
        fields = [
            "salesman_id",
            "customer_id",
            "status",
            "date_created",
            "date_updated",
            "amount",
            "payment_due",
        ]

        read_only_fields = [
            'id',
            "date_created",
            "date_updated",
            "customer_id",
        ]
