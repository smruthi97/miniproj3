📦 Courier Management System (Django)

A mini-project built using the Django Framework to automate courier booking, shipment tracking, and secure online payment. The system enables customers to book couriers and make payments via PayPal, while admins manage shipment details and track progress efficiently.

🚀 Features

User registration & login

Courier booking with sender & receiver details

Auto-generated tracking number

Track shipment status (Booked → In-Transit → Delivered)

Online payment using PayPal

Admin dashboard for full management

View past courier history

Error-free digital record system

🛠️ Technologies Used

Backend: Python Django

Frontend: HTML, CSS, Bootstrap

Payment Gateway: PayPal

Database: SQLite / MySQL (update if using MySQL)

📌 Modules Included
Module	Description
User Authentication	Secure login using Django Auth
Courier Booking	Add parcel + customer details
PayPal Payment	Online payment integration
Shipment Tracking	Search status using tracking ID
Admin Panel	CRUD operations on shipments
Reports	View booking and payment history
📦 Installation & Setup
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Database Setup
python manage.py makemigrations
python manage.py migrate

3️⃣ PayPal Configuration

In settings.py, update:

PAYPAL_CLIENT_ID = "YOUR_PAYPAL_CLIENT_ID"
PAYPAL_CLIENT_SECRET = "YOUR_PAYPAL_SECRET_KEY"


Enable PayPal sandbox mode for testing.

4️⃣ Create Superuser
python manage.py createsuperuser

5️⃣ Run the Project
python manage.py runserver


✅ Now open in browser:

http://127.0.0.1:8000/


Admin Login:

http://127.0.0.1:8000/admin/

📁 Project Structure
courier-management-system/
│── cms/                # Django project folder
│── courier/            # Main app
│── templates/          # HTML templates
│── static/             # CSS & JS files
│── db.sqlite3          # Database file
│── manage.py
│── README.md

🔑 Roles & Permissions
Role	Permissions
Admin	Update delivery status, manage bookings & payments
User	Book courier, make payment & check status
🎯 Outcomes

Automates courier booking and payments

Improves customer satisfaction with easy tracking

Eliminates cash handling and delays

🤝 Contributing

Fork the repo, make improvements, and submit a pull request!

📜 License

This project is open-source for educational usage.
