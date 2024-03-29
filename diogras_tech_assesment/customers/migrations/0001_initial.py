# Generated by Django 4.2.9 on 2024-02-01 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.TextField()),
                ("last_name", models.TextField()),
                ("address", models.TextField()),
                ("city", models.TextField()),
                ("zipcode", models.TextField()),
                ("state", models.TextField()),
            ],
        ),
    ]
