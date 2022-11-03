from django.shortcuts import render, HttpResponse
from . import models

def booking_details(request, booking_id):
    booking_instance = models.Booking.objects.get(pk=booking_id)
    response = "You're looking for booking {}. The room is {}.".format(booking_id, booking_instance.room)
    return HttpResponse(response)