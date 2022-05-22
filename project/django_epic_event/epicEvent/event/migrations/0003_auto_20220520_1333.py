# Generated by Django 4.0.4 on 2022-05-20 13:33

from django.db import migrations


def create_status(apps, shema_migration):
    STATUS = apps.get_model("event.EventStatus")
    status_available = [
        "DRAFT",
        "STARTED",
        "CLOSED",
    ]

    for stat in status_available:
        STATUS.objects.create(title=stat)



class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_alter_event_description'),
    ]

    operations = [
        migrations.RunPython(create_status),
    ]