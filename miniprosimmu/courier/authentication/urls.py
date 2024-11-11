from django.contrib import admin
from django.urls import path,include
from .import views



urlpatterns = [
    path('',views.index,name="index"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('index',views.index,name="index"),
    path('logout/', views.user_logout_view, name='logout'),
    path('logout1/', views.user_logout_view1, name='logout1'),
    # path('register_staff/', views.register_staff, name='register_staff'),
    path('sign-in/', views.sign_in_staff, name='sign_in_staff'),    # URL for staff sign-in
    path('staff_home/', views.staff_home, name='staff_home'),  
]