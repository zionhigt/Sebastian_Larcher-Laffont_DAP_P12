from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(max_length=200)
    date_event = models.DateTimeField("date_event", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_contact_id = models.ForeignKey(
        "authentication.User",
        related_name="support_contact",
        on_delete=models.CASCADE
    )
    contrat_id = models.ForeignKey("contrat.Contrat", related_name="contrat", on_delete=models.CASCADE)
    status = models.ForeignKey("event.EventStatus", related_name="avent_status", on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["contrat_id"], name="unique_contrat")
        ]


class EventStatus(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self):
        return self.title
