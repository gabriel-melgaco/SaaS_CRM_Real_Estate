# Generated by Django 5.1.5 on 2025-02-04 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_app', '0003_client_company_name_client_dns_name_client_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='name',
            new_name='complete_name',
        ),
        migrations.AddField(
            model_name='client',
            name='cpf',
            field=models.IntegerField(default='139888615', unique=True),
            preserve_default=False,
        ),
    ]
