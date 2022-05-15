from rest_framework.serializers import ModelSerializer
from event.models import Event


class EventListSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = ['id',]


class EventUpdateSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = ['id',]


class EventDetailSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = [
            'id',
        ]

        read_only_fields = [
            'id',
        ]