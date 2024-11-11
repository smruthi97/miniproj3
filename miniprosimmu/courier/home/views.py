from django.shortcuts import render, redirect,  get_object_or_404
from django.http import HttpResponse
from .models import CourierBooking
from django.contrib.auth.decorators import login_required
from authentication.models import Register
from django.utils import timezone
from django.contrib import messages
from authentication.models import Staff_Detail
def index(request):
    return render(request,"index.html")

def userhome(request):
     # Get the username from the session
    username = request.session.get('username')  # Use .get() to avoid KeyError if not set

    # If the username is available, show a welcome message
    # if username:
    #     messages.success(request, f"Welcome, {username}!")

    # Pass the username to the template
    context = {
        'username': username
    }
    return render(request,"userhome.html", context)


from django.shortcuts import render, redirect
from .models import Register, CourierBooking
from django.utils import timezone
from django.http import HttpResponse
from datetime import timedelta


def book_courier(request):
    if request.method == "POST":
        # Get form data
        sender_name = request.POST.get('sender_name')
        pickup_address = request.POST.get('pickup_address')
        pickup_city = request.POST.get('pickup_city')
        receiver_name = request.POST.get('receiver_name')
        receiver_phone = request.POST.get('receiver_phone')
        receiver_email = request.POST.get('receiver_email')
        destination_address = request.POST.get('destination_address')
        destination_city = request.POST.get('destination_city')
        destination_pincode = request.POST.get('destination_pincode')
        weight = float(request.POST.get('weight', 0))
        item_type = request.POST.get('item_type')
        pickup_date = request.POST.get('pickup_date')

       

        # Pricing logic based on weight and item type
        base_price_per_kg = 10  # Example base price per kg
        extra_charges = {
            "Fresh Items": 3,
            "Breakables": 5,
            "Health Supplies": 2,
            "Everyday Goods": 0
        }
        price = (weight * base_price_per_kg) + extra_charges.get(item_type, 0)

        # Get the item photo file from request.FILES
        item_photo = request.FILES.get('item_photo')

        # Get the logged-in user's instance from the Register model
        username = request.session.get('username')
        user = Register.objects.filter(username=username).first()

        # Create and save the CourierBooking instance
        booking = CourierBooking.objects.create(
            sender_name=sender_name,
            pickup_address=pickup_address,
            pickup_city=pickup_city,
            receiver_name=receiver_name,
            receiver_phone=receiver_phone,
            receiver_email=receiver_email,
            destination_address=destination_address,
            destination_city=destination_city,
            destination_pincode=destination_pincode,
            weight=weight,
            item_type=item_type,
            price=price,
            pickup_date=pickup_date,
            item_photo=item_photo,
            user=user
        )

        # Redirect to payment page with booking details
        return redirect('payment', price=price, tracking_id=booking.tracking_id)

    # Render the booking form if the request method is GET
    return render(request, 'book_courier.html')


def payment(request, price,tracking_id):
    booking = get_object_or_404(CourierBooking, tracking_id=tracking_id)
    price = booking.price  # Get the price from the booking

    return render(request, 'payment.html', {
        'price': price,
        'booking': booking,
    })

def success(request, tracking_id):

     
    # Fetch the booking details using the tracking_id
    booking = get_object_or_404(CourierBooking, tracking_id=tracking_id)
    # Update the status to 'Paid'
    booking.status = 'Paid'
    booking.save()
    # Get the payment date (you can pass it as needed)
    payment_date = timezone.now().date() # Define how to get the payment date
    # Receipt.objects.create(
    #     booking=booking,
    #     tracking_id=tracking_id,
    #     amount_paid=booking.price,
    #     payment_date=payment_date
    # )
    return render(request, 'success.html', {
        'booking': booking,
        'payment_date': payment_date,
    })


def courier_details_view(request):
    # Get the user based on the username in the session
    username = request.session['username']  # Assume user is logged in
    user = Register.objects.get(username=username)
    
    # Retrieve booking details for this user
    bookings = CourierBooking.objects.filter(user=user)
    
    # Pass the booking details to the template
    context = {
        'bookings': bookings,
        'username': username  # Pass username to display on the page if needed
    }
    
    return render(request, 'courier_details.html', context)

def pickups(request):
    employee_id = request.session.get('employee_id')  # Get employee_id from session
    staff_location = 'Unknown Location'  # Default value for staff location
    staff_name = 'Guest'  # Default value for staff name

    if employee_id:  # Check if employee_id exists in session
        try:
            # Attempt to get the staff member using the employee_id
            staff_member = Staff_Detail.objects.get(employee_id=employee_id)
            staff_location = staff_member.location  # Get staff's location
            staff_name = staff_member.staff_name  # Get staff member's name
        except Staff_Detail.DoesNotExist:
            staff_location = 'Unknown Location'  # Handle case where staff member is not found

    bookings = CourierBooking.objects.all()  # Get all booking records

    context = {
        'bookings': bookings,  # Pass the list of bookings to the template
        'staff_location': staff_location,  # Pass the staff's location to the template
        'staff_name': staff_name,  # Pass the staff's name to the template
    }
    
    return render(request, 'pickups.html', context)


def booking_details(request, tracking_id):
    booking = get_object_or_404(CourierBooking, tracking_id=tracking_id)
    return render(request, 'booking_details.html', {'booking': booking})

from django.http import JsonResponse
import json
def pickup_courier(request):
    if request.method == 'POST':
        data = json.loads(request.body)  # Load the JSON data
        tracking_id = data.get('tracking_id')
        staff_name = data.get('staff_name')

        try:
            # Retrieve the booking record based on the tracking ID
            booking = CourierBooking.objects.get(tracking_id=tracking_id)

            # Update the booking record with the staff name
            booking.picked_by = staff_name
            booking.picked_status = True  # Set picked status to True
            booking.save()  # Save the changes to the database

            return JsonResponse({'success': True, 'message': 'Pickup recorded successfully.'})
        except CourierBooking.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Tracking ID not found.'})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})




def deliveries(request):
    employee_id = request.session.get('employee_id')  # Get employee_id from session
    staff_location = 'Unknown Location'  # Default value for staff location
    staff_name = 'Guest'  # Default value for staff name

    if employee_id:  # Check if employee_id exists in session
        try:
            # Attempt to get the staff member using the employee_id
            staff_member = Staff_Detail.objects.get(employee_id=employee_id)
            staff_location = staff_member.location  # Get staff's location
            staff_name = staff_member.staff_name  # Get staff member's name
        except Staff_Detail.DoesNotExist:
            # Handle case where the staff member is not found (Optional: You can log an error or return a message)
            staff_location = 'Unknown Location'
            staff_name = 'Guest'
    
    bookings = CourierBooking.objects.filter(picked_status=True)  # Get all bookings where pickup_status is True
    context = {
        'bookings': bookings,  # Pass the list of bookings to the template
        'staff_location': staff_location,  # Pass the staff's location to the template
        'staff_name': staff_name,  # Pass the staff's name to the template
    }
    
    return render(request, 'deliveries.html', context)


# Mark the booking as delivered
def mark_as_delivered(request):
    if request.method == 'POST':
        # Parse the JSON data from request body
        data = json.loads(request.body)
        tracking_id = data.get('tracking_id')
        staff_name = data.get('staff_name')
        staff_location = data.get('staff_location')

        # Check if staff name and location are provided
        if not staff_name or not staff_location:
            return JsonResponse({'success': False, 'message': 'Missing staff name or location.'}, status=400)

        try:
            # Retrieve the booking by tracking ID
            booking = CourierBooking.objects.get(tracking_id=tracking_id)

            # Check if the staff is at the delivery location
            if booking.destination_city == staff_location:
                # Update the booking status to "Delivered" and record delivery details
                booking.delivery_status = "Delivered"
                booking.delivered_by = staff_name
                booking.delivered_date = timezone.now()
                booking.save()
                return JsonResponse({'success': True, 'message': 'Marked as delivered.'})
            else:
                return JsonResponse({'success': False, 'message': 'You are not at the delivery location.'})

        except CourierBooking.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Booking not found.'}, status=404)

    # If the method is not POST
    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)

# Mark the booking as Out for Delivery
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CourierBooking
@csrf_exempt
def mark_out_for_delivery(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request
            data = json.loads(request.body)
            tracking_id = data.get('tracking_id')
            staff_name = data.get('staff_name')
            staff_location = data.get('staff_location')  # Get the staff's current location from the request
            print(f"Tracking ID: {tracking_id}, Staff: {staff_name}, Location: {staff_location}")

            # Fetch the courier booking by tracking_id
            booking = CourierBooking.objects.get(tracking_id=tracking_id)

            # Check if the staff's location matches the destination city
            if staff_location == booking.destination_city:
                # Update the status to "Out for Delivery" and set the staff name
                booking.delivery_status = 'Out for Delivery'
                booking.delivered_by = staff_name  # Staff who marked it out for delivery
                booking.save()

                return JsonResponse({"success": True, "message": "The courier has been marked as 'Out for Delivery'."})
            else:
                # If the staff is not at the correct location, return an error message
                return JsonResponse({"success": False, "message": "You are not in the correct location to deliver this courier."}, status=400)

        except CourierBooking.DoesNotExist:
            return JsonResponse({"success": False, "message": "Courier not found."}, status=404)
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)}, status=500)

    # If the method is not POST
    return JsonResponse({"success": False, "message": "Invalid request method."}, status=405)


def view_full_details(request, tracking_id):
    # Fetch the full booking details using tracking_id
    booking = get_object_or_404(CourierBooking, tracking_id=tracking_id)
    
    # Render the booking details in the template
    return render(request, 'full_booking_details.html', {'booking': booking})