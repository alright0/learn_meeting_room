from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date


class CustomUser(AbstractUser):
    OFFICE_MANAGER = 1
    EMPLOYEE = 2

    ROLE_CHOICES = (
          (OFFICE_MANAGER, 'Office manager'),
          (EMPLOYEE, 'Employee'),
    )

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES,
                                            blank=True, null=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return self.username


class Room(models.Model):
    name = models.CharField(max_length=100)
    chairs_number = models.IntegerField()
    projector = models.BooleanField()
    marker_board = models.BooleanField()

    def __str__(self):
        return self.name

    def get_last_booking(self):        
        last_booking = Booking.objects.filter(room=self.pk)
        max_date_to = last_booking.latest("date_to").date_to
        last_booking = last_booking.filter(date_to=max_date_to)
        max_time_to = last_booking.latest("time_to").time_to
        last_booking = last_booking.filter(time_to=max_time_to)
        if last_booking:
            last_booking_str = "Is booked by " + str( last_booking[0] )
        else:
            last_booking_str = "Not booked yet!"    
        return last_booking_str

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_from = models.DateField(default=date.today)
    time_from = models.TimeField(default="00:00")
    date_to = models.DateField(default=date.today,)
    time_to = models.TimeField(default="00:00")

    def __str__(self):
        booking_str = str(self.user) + " from " + str(self.date_from) + " " \
         + str(self.time_from)[:5] + " to " + str(self.date_to) + " " + str(self.time_to)[:5]
        return booking_str
        