# Generated by Django 5.1.7 on 2025-03-20 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("huaqi", "0005_processedpredrawdown_1_processedpredrawdown_3_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="news_2024",
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
                ("Title", models.TextField()),
                ("Date", models.DateField()),
                ("Content", models.TextField()),
                ("Countries", models.TextField()),
            ],
        ),
    ]
