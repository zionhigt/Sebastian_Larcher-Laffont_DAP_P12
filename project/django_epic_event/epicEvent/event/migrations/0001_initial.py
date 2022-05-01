# Generated by Django 4.0.4 on 2022-04-24 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contrat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('contrat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contrat', to='contrat.contrat')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avent_status', to='event.eventstatus')),
                ('support_contact_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='support_contact', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='event',
            constraint=models.UniqueConstraint(fields=('contrat_id',), name='unique_contrat'),
        ),
    ]
