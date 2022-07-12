# Generated by Django 4.0.6 on 2022-07-09 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=15)),
                ('staff_number', models.IntegerField()),
                ('appointment_start_date', models.DateField()),
                ('tin', models.CharField(max_length=255)),
                ('ssnit', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('title', models.CharField(max_length=6)),
                ('surname', models.CharField(max_length=255)),
                ('other_names', models.CharField(max_length=255)),
                ('gender_code', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=1)),
                ('marital_status', models.CharField(choices=[('M', 'M'), ('S', 'S')], max_length=1)),
                ('phone', models.CharField(max_length=16)),
                ('address', models.CharField(max_length=255)),
                ('passport_photo', models.ImageField(upload_to='media/passport-photo/')),
                ('employment_date', models.DateField()),
                ('designation', models.CharField(blank=True, max_length=255, null=True)),
                ('job_grade', models.CharField(blank=True, max_length=255, null=True)),
                ('employee_type', models.CharField(choices=[('Permanent', 'Permanent'), ('Contract', 'Contract')], max_length=255)),
                ('branch', models.CharField(max_length=255)),
                ('hod_name', models.CharField(max_length=255)),
                ('contract_freq_code', models.CharField(max_length=255)),
                ('contract_duration', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
