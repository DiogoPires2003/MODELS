# Generated by Django 5.0.6 on 2025-02-26 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='car_photos/'),
        ),
    ]
