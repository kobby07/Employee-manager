# Generated by Django 4.0.6 on 2022-07-10 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_employee_type_employee_employment_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='marital_status',
            field=models.CharField(choices=[('Married', 'Married'), ('Single', 'Single')], max_length=15),
        ),
    ]