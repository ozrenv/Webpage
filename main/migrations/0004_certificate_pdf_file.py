# Generated by Django 4.2.5 on 2023-10-19 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_certificate"),
    ]

    operations = [
        migrations.AddField(
            model_name="certificate",
            name="pdf_file",
            field=models.FileField(
                blank=True, null=True, upload_to="certificates/pdfs/"
            ),
        ),
    ]
