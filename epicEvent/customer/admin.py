from django.contrib import admin
from customer.models import Customer


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

    def get_form(self, request, obj=None, change=False, **kwargs):
        return super().get_form(request, obj, change, **kwargs)


admin.site.register(Customer, CustomerAdmin)
