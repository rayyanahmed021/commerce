# Generated by Django 3.1 on 2020-08-28 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0028_bidding_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidding',
            name='bid',
            field=models.IntegerField(blank=True),
        ),
    ]
