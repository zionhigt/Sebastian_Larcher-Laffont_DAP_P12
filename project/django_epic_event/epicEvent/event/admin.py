from django.contrib import admin
from event.models import Event

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

admin.site.register(Event, EventAdmin)
