# Generated by Django 3.1 on 2020-08-29 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0032_auto_20200828_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='winner',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winner', to=settings.AUTH_USER_MODEL),
        ),
    ]
