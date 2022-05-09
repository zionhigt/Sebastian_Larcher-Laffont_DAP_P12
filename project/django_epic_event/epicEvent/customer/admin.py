from django.contrib import admin
from customer.models import Customer

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "email",
        "date_created",
        "date_updated",
        "sale_contact_id",
        "status",
        "mobile",
        "phone",
]

admin.site.register(Customer, CustomerAdmin)
