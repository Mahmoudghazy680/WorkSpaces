# Generated by Django 5.0.6 on 2024-05-31 20:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("space", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="desk",
            name="branch",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="space.branch",
                verbose_name="Branch Name",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="desk",
            name="space",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="space.space",
                verbose_name="Space",
            ),
        ),
    ]
