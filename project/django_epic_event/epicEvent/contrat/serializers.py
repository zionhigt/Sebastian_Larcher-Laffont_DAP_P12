from rest_framework.serializers import ModelSerializer
from contrat.models import Contrat


class ContratListSerializer(ModelSerializer):

    class Meta:
        model = Contrat
        fields = ['id',]


class ContratUpdateSerializer(ModelSerializer):

    class Meta:
        model = Contrat
        fields = ['id',]


class ContratDetailSerializer(ModelSerializer):

    class Meta:
        model = Contrat
        fields = [
            'id',
        ]

        read_only_fields = [
            'id',
        ]