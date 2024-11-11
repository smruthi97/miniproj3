from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name='home'),
    path('book-courier/', views.book_courier, name='book_courier'),
    path('success/<str:tracking_id>', views.success, name='success'),
    path('userhome/', views.userhome, name='userhome'),
    path('payment/<str:price>/<str:tracking_id>/', views.payment, name='payment'),
    path('courier-details/', views.courier_details_view, name='courier_details'),
    path('pickups/', views.pickups, name='pickups'),  
    
    path('booking-details/<str:tracking_id>/', views.booking_details, name='booking_details'),
    path('pickup-courier/', views.pickup_courier, name='pickup_courier'), 
    path('mark_as_delivered/', views.mark_as_delivered, name='mark_as_delivered'),
    path('deliveries/', views.deliveries, name='deliveries'),
    path('mark_out_for_delivery/', views.mark_out_for_delivery, name='mark_out_for_delivery'),
    path('view_full_details/<str:tracking_id>/', views.view_full_details, name='view_full_details'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
