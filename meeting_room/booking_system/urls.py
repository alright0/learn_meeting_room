from django.urls import path
from . import views


urlpatterns = [
    path('t_booking_list/', views.t_booking_list),
    path('booking_list/', views.booking_list),
    path('t_booking_details/<int:booking_id>/', views.booking_details,
         name='details'),
]
