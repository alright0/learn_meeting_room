from django.db import models
from django.contrib.auth.models import AbstractUser


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

    def __str__(self):
        return self.name


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
