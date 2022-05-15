from rest_framework.serializers import ModelSerializer
from event.models import Event


class EventListSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = [
            'id',
            'name',
            'support_contact_id',
            'contrat_id',
            'status',
        ]


class EventUpdateSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = [
            'name',
            'description',
            'support_contact_id',
            'status',
        ]


class EventDetailSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = [
            'id',
            'name',
            'description',
            'date_created',
            'date_updated',
            'support_contact_id',
            'contrat_id',
            'status',
        ]

        read_only_fields = [
            'id',
            'date_created',
            'date_updated',
            'contrat_id',
        ]