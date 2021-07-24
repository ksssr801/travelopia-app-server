from rest_framework import serializers
from .models import BookingDetails

class BookingDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookingDetails
        fields = '__all__'