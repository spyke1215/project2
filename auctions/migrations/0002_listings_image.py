# Generated by Django 3.0.8 on 2020-08-05 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='image',
            field=models.CharField(max_length=2048, null=True),
        ),
    ]