# Generated by Django 5.0.6 on 2024-05-25 12:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("space", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="password",
        ),
    ]