# Generated by Django 5.0.6 on 2024-05-25 13:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("space", "0002_remove_customer_password"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="space",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="space.space",
                verbose_name="Space",
            ),
        ),
    ]
