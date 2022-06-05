from rest_framework.serializers import ModelSerializer
from customer.models import Customer


class CustomerListSerializer(ModelSerializer):

    class Meta:
        model = Customer
        fields = [
            'id',
            "first_name",
            "last_name",
            "company_name",
            "sale_contact_id",
            "status",
        ]


class CustomerUpdateSerializer(ModelSerializer):

    class Meta:
        model = Customer
        fields = [
            "first_name",
            "last_name",
            "company_name",
            "sale_contact_id",
            "status",
            "mobile",
            "phone",
        ]


class CustomerDetailSerializer(ModelSerializer):

    class Meta:
        model = Customer
        fields = [
            'id',
            "first_name",
            "last_name",
            "email",
            "company_name",
            "sale_contact_id",
            "status",
            "mobile",
            "phone",
            "date_created",
            "date_updated",
        ]

        read_only_fields = [
            'id',
            "date_created",
            "date_updated",
        ]
