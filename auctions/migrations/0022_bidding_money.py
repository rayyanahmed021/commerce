# Generated by Django 3.1 on 2020-08-28 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0021_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='bidding',
            name='money',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='money', to='auctions.user'),
            preserve_default=False,
        ),
    ]
