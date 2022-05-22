from django.contrib import admin
from contrat.models import Contrat
from authentication.models import User

# Register your models here.

class ContratAdmin(admin.ModelAdmin):
    list_display = [
        "customer_id",
        "salesman_id",
        "date_created",
        "date_updated",
        "status",
        "amount",
        "payment_due",
    ]

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.base_fields.get("salesman_id").queryset = User.objects.filter(role__name="SALESMAN")
        return form

admin.site.register(Contrat, ContratAdmin)
