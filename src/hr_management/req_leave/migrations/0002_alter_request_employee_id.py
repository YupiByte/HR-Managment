# Generated by Django 4.2.6 on 2023-11-19 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('req_leave', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='employee_id',
            field=models.CharField(max_length=150),
        ),
    ]
