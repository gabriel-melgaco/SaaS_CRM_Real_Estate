# Generated by Django 5.1.5 on 2025-03-08 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_app', '0013_resetpassword'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassword',
            name='token',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
