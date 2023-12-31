# Generated by Django 4.2.5 on 2023-10-19 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_blog_contactprofile_media_portfolio_skill_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Certificate",
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
                ("date", models.DateTimeField(blank=True, null=True)),
                ("name", models.CharField(blank=True, max_length=50, null=True)),
                ("title", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Certificate",
                "verbose_name_plural": "Certificates",
            },
        ),
    ]
