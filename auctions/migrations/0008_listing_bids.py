# Generated by Django 3.1 on 2020-08-27 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_remove_watchlist_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='bids',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='auctions.bidding'),
            preserve_default=False,
        ),
    ]