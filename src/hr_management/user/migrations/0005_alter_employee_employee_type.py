# Generated by Django 4.2.6 on 2023-12-15 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_employee_employee_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_type',
            field=models.CharField(choices=[('Chief Executive Officer', 'Chief Executive Officer'), ('Chief Financial Officer', 'Chief Financial Officer'), ('Chief Operating Officer', 'Chief Operating Officer'), ('Chief Marketing Officer', 'Chief Marketing Officer'), ('Chief Technology Officer', 'Chief Technology Officer'), ('Vice President', 'Vice President'), ('Director', 'Director'), ('Manager', 'Manager'), ('Administrator', 'Administrator'), ('Engineer', 'Engineer'), ('Sales', 'Sales'), ('Other', 'Other')], max_length=30),
        ),
    ]
