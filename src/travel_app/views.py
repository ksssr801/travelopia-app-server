from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import BookingDetailsSerializers
from .models import BookingDetails
from .utils.utility import *
from .utils.default_config import *

class TravelAppViewSet(viewsets.ModelViewSet):
    serializer_class = BookingDetailsSerializers

    def get_queryset(self):
        return BookingDetails.objects.all()

    @action(detail=False, methods=['post'], name="do_booking", url_path='do-booking')
    def get_booking_info(self, request):
        try:
            print ("request : ", request.data)
            data_obj = request.data
            
            return Response({}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['get'], name="booking_details", url_path='booking-details')
    def get_booking_details(self, request):
        try:
            print ("request : ", request.GET, get_ID(), DESTINATION_LIST)
            all_booking_details = BookingDetails.objects.all()
            serialize_data = BookingDetailsSerializers(all_booking_details, many=True).data
            print ("serialize_data : ", serialize_data)
            return Response(serialize_data, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(serialize_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    