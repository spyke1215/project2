# Generated by Django 3.0.8 on 2020-08-09 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20200809_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='closed',
            field=models.BooleanField(default=False),
        ),
    ]