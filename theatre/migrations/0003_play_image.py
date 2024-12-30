# Generated by Django 5.1.4 on 2024-12-26 14:07

import theatre.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("theatre", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="play",
            name="image",
            field=models.ImageField(
                null=True, upload_to=theatre.models.play_image_file_path
            ),
        ),
    ]
