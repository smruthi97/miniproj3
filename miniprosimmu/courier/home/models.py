

# Create your models here.
import random

from django.db import models
from django.contrib.auth.models import User
from authentication.models import Register

class CourierBooking(models.Model):
      
    CITY_CHOICES = [
        ('Alappuzha', 'Alappuzha'),
        ('Idukki', 'Idukki'),
        ('Ernakulam', 'Ernakulam'),
        ('Kottayam', 'Kottayam'),
        ('Kozhikode', 'Kozhikode'),
        ('Malappuram', 'Malappuram'),
        ('Palakkad', 'Palakkad'),
        ('Pathanamthitta', 'Pathanamthitta'),
        ('Thiruvananthapuram', 'Thiruvananthapuram'),
        ('Kollam', 'Kollam'),
        ('Kannur', 'Kannur'),
        ('Wayanad', 'Wayanad'),
        ('Kasargod', 'Kasargod'),
        ('Thrissur', 'Thrissur'),
        # Add other cities here...
    ]
    sender_name = models.CharField(max_length=100)  # Add sender's name
    pickup_address = models.TextField()  # Sender's address
    pickup_city = models.CharField(max_length=100, choices=CITY_CHOICES)
    receiver_name = models.CharField(max_length=100)
    receiver_phone = models.CharField(max_length=10)  # 10-digit receiver's phone number
    receiver_email = models.EmailField()  # Receiver's email address
    destination_address = models.TextField()  # Receiver's address
    destination_city = models.CharField(max_length=100, choices=CITY_CHOICES)
    destination_pincode = models.CharField(max_length=6)  # 6-digit pincode
   
    # package_details = models.TextField()  # Details about the package
    weight = models.DecimalField(max_digits=5, decimal_places=2)  # Weight of the package
    item_type = models.CharField(max_length=50, choices=[('Fresh Items', 'Fresh Items'), ('Breakables', 'Breakables'), ('Health Supplies', 'Health Supplies'), ('Everyday Goods', 'Everyday Goods')])  # Type of item
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)  # Calculated shipping price
    tracking_id = models.CharField(max_length=6, unique=True, editable=False)  # 6-digit tracking ID
    picked_by = models.CharField(max_length=255, blank=True, null=True)  # Field to store the staff name who picked the courier
    picked_status = models.BooleanField(default=False) 

    def save(self, *args, **kwargs):
        if not self.tracking_id:
            self.tracking_id = self.generate_unique_tracking_id()
        super().save(*args, **kwargs)

    def generate_unique_tracking_id(self):
        while True:
            tracking_id = str(random.randint(100000, 999999))  # Generates a 6-digit number
            if not CourierBooking.objects.filter(tracking_id=tracking_id).exists():
                return tracking_id
            
    status = models.CharField(max_length=20, default='Pending')  # Courier status (Pending, Picked Up, etc.)
    pickup_date = models.DateField()  # Scheduled pickup date
    item_photo = models.ImageField(upload_to='item_photos/', null=True, blank=True)  # Field to upload item photo
    user = models.ForeignKey(Register, on_delete=models.CASCADE)
    DELIVERY_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Picked Up', 'Picked Up'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),  # You can add any other status if needed
    ]

    delivery_status = models.CharField(max_length=20, choices=DELIVERY_STATUS_CHOICES, default='Pending')  # Courier delivery status (Pending, Picked Up, Out for Delivery, Delivered, etc.)
    delivered_by = models.CharField(max_length=255, blank=True, null=True)  # Staff name who delivered the package (optional)
    delivery_date = models.DateField(null=True, blank=True)  # Optional delivery date (null if not delivered)
    def __str__(self):
        return f"{self.sender_name} - {self.tracking_id}"


