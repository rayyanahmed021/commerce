# Generated by Django 3.1 on 2020-08-28 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0023_auto_20200828_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidding',
            name='starting',
            field=models.IntegerField(default=20),
        ),
    ]
