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
        qs = Booking.objects.all().select_related('room', 'user')
        booking = {}
        for i in qs:
            if i.room_id in booking:
                if i.date_to > booking[i.room_id].date_to or \
                   ( i.date_to == booking[i.room_id].date_to  and
                     i.time_to >= booking[i.room_id].time_to ): 
                    booking[i.room_id] = i
            else:
                booking[i.room_id] = i
        for b in booking.values():
            b.full_name = f" {str(b.user)} from {str(b.date_from)}   \
                            {str(b.time_from)[:5]} to {str(b.date_to)} \
                            {str(b.time_to)[:5]}" 
        data = {"rooms": rooms,
                "booking": booking}
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


def get_last_booking(room):
    #last_booking = Booking.objects.latest("date_to").latest("time_to").filter(room=room.pk)
    last_booking = Booking.objects.filter(room=room.pk)
    if not last_booking:
        return "Not booked yet!"
    #max_date_to = last_booking.latest("date_to").date_to
    #last_booking = last_booking.filter(date_to=max_date_to)
    #max_time_to = last_booking.latest("time_to").time_to
    #last_booking = last_booking.filter(time_to=max_time_to)
    if last_booking:
        last_booking_str = "Is booked by " + str(last_booking[0])
    else:
        last_booking_str = "Not booked yet!"
    return last_booking_str
