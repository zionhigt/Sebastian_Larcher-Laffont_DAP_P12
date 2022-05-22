from django.contrib import admin
from customer.models import Customer
from authentication.models import User
from customer.permissions import IsAuthorOrReadOnly
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
    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj=None, change=False, **kwargs)
        form.base_fields.get("sale_contact_id").queryset = User.objects.filter(role__name="SALESMAN")
        # print(obj.sale_contact_id.id, request.user.id, request.user.role.name != "MANAGER")
        form.base_fields['field'].widget.attrs['readonly'] = True
        # if obj.sale_contact_id.id != request.user.id or request.user.role.name != "MANAGER":
        #     self.readonly_fields = tuple(form.base_fields.keys())
        return form

admin.site.register(Customer, CustomerAdmin)