# Generated by Django 5.0.2 on 2024-02-16 05:09

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("House_Price_model", "0002_delete_get_data_from_user_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="test",
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
                ("price", models.FloatField()),
            ],
        ),
    ]
