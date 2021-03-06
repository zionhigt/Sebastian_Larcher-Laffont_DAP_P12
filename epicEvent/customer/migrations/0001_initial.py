# Generated by Django 4.0.4 on 2022-04-24 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('mobile', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('sale_contact_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sale_contact', to=settings.AUTH_USER_MODEL, verbose_name='sale_contact')),
                ('status', models.BooleanField(default=False, verbose_name='status')),
            ],
        ),
        migrations.AddConstraint(
            model_name='customer',
            constraint=models.UniqueConstraint(fields=('email',), name='unique_customer'),
        ),
    ]
