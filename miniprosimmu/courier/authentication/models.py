from django.db import models


# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    email=models.EmailField()
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    def __str__(self):
     return self.name


# models.py

from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator
from django.contrib.auth.hashers import make_password

class Staff_Detail(models.Model):
   
    staff_name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=100)
    phone = models.CharField(
        max_length=10,
        validators=[RegexValidator(regex=r'^\d{10}$', message='Enter a valid 10-digit phone number')],
        unique=True
    )
    code = models.CharField(max_length=4)
    location = models.CharField(
        max_length=50,
        choices=[
            ('Thiruvananthapuram', 'Thiruvananthapuram'),
            ('Kollam', 'Kollam'),
            ('Pathanamthitta', 'Pathanamthitta'),
            ('Alappuzha', 'Alappuzha'),
            ('Kottayam', 'Kottayam'),
            ('Idukki', 'Idukki'),
            ('Ernakulam', 'Ernakulam'),
            ('Thrissur', 'Thrissur'),
            ('Palakkad', 'Palakkad'),
            ('Malappuram', 'Malappuram'),
            ('Kozhikode', 'Kozhikode'),
            ('Wayanad', 'Wayanad'),
            ('Kannur', 'Kannur'),
            ('Kasaragod', 'Kasaragod')
        ]
    )
    

    def __str__(self):
        return self.staff_name