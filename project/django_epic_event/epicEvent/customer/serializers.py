from rest_framework.serializers import ModelSerializer
from customer.models import Customer


class CustomerListSerializer(ModelSerializer):

    class Meta:
        model = Customer
        fields = ['id',]


class CustomerUpdateSerializer(ModelSerializer):

    class Meta:
        model = Customer
        fields = ['id',]


class CustomerDetailSerializer(ModelSerializer):

    class Meta:
        model = Customer
        fields = [
            'id',
        ]

        read_only_fields = [
            'id',
        ]