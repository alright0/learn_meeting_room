class MakeBookingNameService:

    @staticmethod
    def create_booking_name(b):
        full_name = f" {str(b.user)} from {str(b.date_from)}   \
                        {str(b.time_from)[:5]} to {str(b.date_to)} \
                        {str(b.time_to)[:5]}"
        return full_name

    @staticmethod
    def get_last_booking_name(qs):
        booking = {}
        for i in qs:
            if i.room_id in booking:
                if i.date_to > booking[i.room_id].date_to or \
                   (i.date_to == booking[i.room_id].date_to and
                        i.time_to >= booking[i.room_id].time_to):
                    booking[i.room_id] = i
            else:
                booking[i.room_id] = i
        for b in booking.values():
            b.full_name = MakeBookingNameService.create_booking_name(b)
        return booking

    @staticmethod
    def get_booking_names(bookings):
        for b in bookings:
            b.full_name = MakeBookingNameService.create_booking_name(b)