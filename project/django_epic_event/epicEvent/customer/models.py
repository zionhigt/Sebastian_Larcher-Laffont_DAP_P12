from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=100, name="email")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    company_name = models.CharField(max_length=25, blank=True, null=True)
    sale_contact_id = models.ForeignKey(
        "authentication.User",
        verbose_name="sale_contact",
        on_delete=models.SET_NULL,
        related_name="sale_contact",
        blank=True,
        null=True
    )
    status = models.BooleanField(default=False, verbose_name="status")
    mobile = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["email"], name="unique_customer")
        ]
