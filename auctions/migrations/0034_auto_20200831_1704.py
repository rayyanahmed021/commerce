# Generated by Django 3.1 on 2020-08-31 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0033_listing_winner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='items',
            field=models.ManyToManyField(blank=True, related_name='items', to='auctions.listing'),
        ),
    ]
