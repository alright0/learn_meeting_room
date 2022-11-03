from django.urls import path
from . import views


urlpatterns = [
    # ex: /booking_system/booking_details/5/
    path('booking_details/<int:booking_id>/', views.booking_details, name='details'),    
]