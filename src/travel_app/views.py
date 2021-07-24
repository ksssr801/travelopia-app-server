from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import BookingDetailsSerializers
from .models import BookingDetails
from .utils.utility import *
from .utils.default_config import *
import time

class TravelAppViewSet(viewsets.ModelViewSet):
    serializer_class = BookingDetailsSerializers

    def get_queryset(self):
        return BookingDetails.objects.all()

    @action(detail=False, methods=['post'], name="do_booking", url_path='do-booking')
    def get_booking_info(self, request):
        try:
            print ("request : ", request.data)
            data_obj = request.data
            booking_details_obj = BookingDetails()
            booking_details_obj.booking_id = get_ID()
            booking_details_obj.traveller = data_obj.get("traveller", '')
            booking_details_obj.email_id = data_obj.get("email_id", '')
            booking_details_obj.destination = data_obj.get("destination", None)
            booking_details_obj.total_travellers = data_obj.get("total_travellers", None)
            booking_details_obj.budget_per_person = data_obj.get("budget_per_person", None)
            booking_details_obj.creation_time = int(time.time())
            booking_details_obj.last_update_time = int(time.time())
            try:
                booking_details_obj.save()
            except Exception as err:
                print ("Failed to save the booking details.")
            return Response({}, status=status.HTTP_200_OK)
        except Exception as err:
            print ("Error in saving the booking details.")
            return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['get'], name="booking_details", url_path='booking-details')
    def get_booking_details(self, request):
        try:
            print ("request : ", request.GET, get_ID(), DESTINATION_LIST)
            all_booking_details = BookingDetails.objects.all()
            serialized_data = BookingDetailsSerializers(all_booking_details, many=True).data
            print ("serialized_data : ", serialized_data)
            return Response(serialized_data, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(serialized_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    