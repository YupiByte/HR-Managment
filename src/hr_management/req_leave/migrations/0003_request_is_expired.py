# Generated by Django 4.2.6 on 2023-12-16 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('req_leave', '0002_alter_request_employee_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='is_expired',
            field=models.BooleanField(default=False),
        ),
    ]
