from django.contrib import admin
from contrat.models import Contrat

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

admin.site.register(Contrat, ContratAdmin)
