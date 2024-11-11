
# Register your models here.
from django.contrib import admin
from .models import CourierBooking

class CourierBookingAdmin(admin.ModelAdmin):
    list_display = (
        'sender_name', 'pickup_city', 'receiver_name', 'receiver_phone', 'destination_city', 
        'destination_pincode', 'weight', 'item_type', 'price', 'status', 'pickup_date', 'tracking_id'
    )
    search_fields = ('sender_name', 'receiver_name', 'receiver_phone', 'tracking_id')
    list_filter = ('item_type', 'status', 'pickup_date', 'pickup_city', 'destination_city')

admin.site.register(CourierBooking, CourierBookingAdmin)
