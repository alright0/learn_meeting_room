from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Booking, Room
from .serializers import BookingSerializer
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


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


@login_required()
def t_booking_list(request):
    if request.method == 'GET':
        bookings = Booking.objects.all().order_by('-date_to')
        data = {"bookings": bookings}
        return render(request, 'booking_system/t_booking_list.html',
                      context=data)


@login_required()
def t_room_list(request):
    if request.method == 'GET':
        rooms = Room.objects.all()
        data = {"rooms": rooms}
        return render(request, 'booking_system/t_room_list.html',
                      context=data)


@login_required()
def t_room_bookings_details(request, pk):
    if request.method == 'GET':
        room = get_object_or_404(Room, pk=pk)                    
        bookings = Booking.objects.filter(room=room.pk).order_by('-date_to')
        data = {"room": room,
                "bookings": bookings}
        return render(request, 'booking_system/t_room_bookings_details.html',
                      context=data)
