from django.db import models

class Contrat(models.Model):
    customer_id = models.ForeignKey("customer.Customer", related_name="customer_id", on_delete=models.CASCADE)
    salesman_id = models.ForeignKey("authentication.User", related_name="salesman", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    amount = models.FloatField()
    payment_due = models.DateTimeField()