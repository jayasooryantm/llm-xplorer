# Generated by Django 4.2.3 on 2024-05-26 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GameTweet",
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
                ("game_name", models.CharField(max_length=100)),
                ("sentiment_type", models.CharField(max_length=20)),
                ("tweet", models.TextField()),
            ],
        ),
    ]
