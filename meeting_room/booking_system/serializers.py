from rest_framework import serializers


class BookingSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    room = serializers.CharField(required=False, allow_blank=True,
                                 max_length=100)
