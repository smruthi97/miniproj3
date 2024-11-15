# Generated by Django 5.1.1 on 2024-11-05 14:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(max_length=100)),
                ('employee_id', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message='Enter a valid 10-digit phone number', regex='^\\d{10}$')])),
                ('location', models.CharField(choices=[('Thiruvananthapuram', 'Thiruvananthapuram'), ('Kollam', 'Kollam'), ('Pathanamthitta', 'Pathanamthitta'), ('Alappuzha', 'Alappuzha'), ('Kottayam', 'Kottayam'), ('Idukki', 'Idukki'), ('Ernakulam', 'Ernakulam'), ('Thrissur', 'Thrissur'), ('Palakkad', 'Palakkad'), ('Malappuram', 'Malappuram'), ('Kozhikode', 'Kozhikode'), ('Wayanad', 'Wayanad'), ('Kannur', 'Kannur'), ('Kasaragod', 'Kasaragod')], max_length=50)),
                ('password', models.CharField(max_length=128, validators=[django.core.validators.MinLengthValidator(6)])),
            ],
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
    ]
