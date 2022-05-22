from rest_framework.serializers import ModelSerializer
from contrat.models import Contrat
from event.models import Event


class ContratListSerializer(ModelSerializer):

    class Meta:
        model = Contrat
        fields = ['id', "customer_id", "salesman_id"]


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

class ContratSignSerializer(ModelSerializer):

    class Meta:
        model = Contrat
        fields = [
            "status",
        ]
    
    def create_event(*args, **kwargs):
        Event.create(**kwargs)

    def update(self, validated_data):
        event = {
            "name": validated_data.get("", ""),
            "description": validated_data.get("", ""),
            "support_contact_id": validated_data.get("", ""),
            "contrat_id": validated_data.get("", ""),
        }
        self.create_event(name, contrat_id, description, )