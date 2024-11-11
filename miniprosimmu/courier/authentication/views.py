from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login
from .models import Register
from django.contrib.auth import logout

def index(request):
    return render(request,"index.html")
def signup(request):
    if request.method=="POST":
         name=request.POST["name"]
         phone=request.POST["phone"]
         email=request.POST["email"]
         username=request.POST["username"]
         password=request.POST["password"]
         myreg=Register(name=name,phone=phone,email=email,username=username,password=password)
         myreg.save()
         return redirect('signin')
    return render(request,'signup.html')

def signin(request):
    if request.method=="POST":
      username=request.POST["username"]
      password=request.POST["password"]
      user=Register.objects.filter(username=username,password=password).first()
      if user is None:
        messages.error(request, 'invalid password or user name')
        return redirect('signin')
      else:
       request.session['username']=username
       return redirect('userhome')
    return render(request, 'signin.html')


def index(request):
    return render(request,"index.html")


def user_logout_view(request):
    logout(request)  # Clear the session
    return redirect('signin')  # Redirect to the login page

def user_logout_view1(request):
    logout(request)  # Clear the session
    return redirect('sign_in_staff')  # Redirect to the login page
# views.py

from django.shortcuts import render, redirect
# from .models import Staff
from django.core.files.storage import default_storage




  # Ensures that only logged-in staff can access this view
def staff_home(request):
    employee_id = request.session.get('employee_id')  # Get employee_id from session
    
    try:
        staff_member = Staff_Detail.objects.get(employee_id=employee_id)
        location = staff_member.location 
    except Staff_Detail.DoesNotExist:
        staff_member = None  # Handle case where staff member is not found
        location = None
    return render(request, 'staff_home.html', {
        'staff_name': staff_member.staff_name if staff_member else 'Guest',  # Handle case for non-existent staff member
        'employee_id': employee_id,
        'location': location if location else 'Unknown Location', 
        
    })

from .models import Staff_Detail
from django.views.decorators.csrf import csrf_exempt



from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.shortcuts import redirect, render

from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from .models import Staff_Detail

def sign_in_staff(request):
    error_message = None  # Initialize error message

    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        code = request.POST.get('code')  # Get the code from POST

        print(f"Attempting login with Employee ID: {employee_id}")

        try:
            staff_member = Staff_Detail.objects.get(employee_id=employee_id)
            print(f"Found staff member: {staff_member.staff_name}")

            # Check if the provided code matches the stored code
            if code == staff_member.code:
                request.session['employee_id'] = staff_member.employee_id  # Save employee_id in session
                return redirect('staff_home')  # Redirect to staff home page
            else:
                error_message = "Invalid code."
                print("Invalid code provided.")
        except Staff_Detail.DoesNotExist:
            error_message = "Employee ID not found."
            print("Employee ID not found.")

    # Render the login form with an error message
    return render(request, 'staff_login.html', {'error_message': error_message})