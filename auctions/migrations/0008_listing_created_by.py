# Generated by Django 3.1.1 on 2020-09-15 06:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listings', to=settings.AUTH_USER_MODEL),
        ),
    ]