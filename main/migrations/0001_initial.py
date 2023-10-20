# Generated by Django 4.2.5 on 2023-09-21 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PersonalInfo",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("bio", models.TextField()),
                ("email", models.EmailField(max_length=100)),
                ("website", models.URLField(blank=True, null=True)),
                (
                    "profile_image",
                    models.ImageField(
                        blank=True, null=True, upload_to="G:\\GITHUB\\Webpage\\images"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SoloProject",
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
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("project_url", models.URLField()),
                (
                    "project_image",
                    models.ImageField(
                        blank=True, null=True, upload_to="G:\\GITHUB\\Webpage\\images"
                    ),
                ),
            ],
        ),
    ]