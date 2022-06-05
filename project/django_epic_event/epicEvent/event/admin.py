from django.contrib import admin
from event.models import Event
from authentication.models import User

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "description",
        "date_created",
        "date_updated",
        "support_contact_id",
        "contrat_id",
        "status",
    ]

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.base_fields.get("support_contact_id").queryset = User.objects.filter(role__name="SUPPORT")
        return form


admin.site.register(Event, EventAdmin)
