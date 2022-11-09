from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Room
from .models import Booking
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


admin.site.register(Room)
admin.site.register(Booking)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('role',)
    list_filter = ('role',)
    search_fields = ('role',)
    ordering = ('role',)


admin.site.register(CustomUser)
