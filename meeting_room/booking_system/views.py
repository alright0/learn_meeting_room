from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer
from django.shortcuts import render, HttpResponse


def booking_details(request, booking_id):
    try:
        booking_instance = Booking.objects.get(pk=booking_id)
    except Booking.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    response = "You're looking for booking {}. The room is {}.".format(
        booking_id, booking_instance.room)
    return HttpResponse(response)


@api_view(['GET'])
def booking_list(request):
    if request.method == 'GET':
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)
