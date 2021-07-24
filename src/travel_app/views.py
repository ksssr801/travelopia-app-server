from rest_framework import status, viewsets
from rest_framework.response import Response
from .serializers import BookingDetailsSerializers
from .models import BookingDetails
from rest_framework.decorators import action

class TravelAppViewSet(viewsets.ModelViewSet):
    serializer_class = BookingDetailsSerializers

    def get_queryset(self):
        return BookingDetails.objects.all()

    @action(detail=False, methods=['post'], name="do_booking", url_path='do-booking')
    def get_booking_info(self, request):
        print ("request : ", request.data)
        return Response({})

    @action(detail=False, methods=['get'], name="booking_details", url_path='booking-details')
    def get_booking_details(self, request):
        print ("request : ", request.GET)
        all_booking_details = BookingDetails.objects.all()
        serialize_data = BookingDetailsSerializers(all_booking_details, many=True).data
        print ("serialize_data : ", serialize_data)
        return Response(serialize_data, status=status.HTTP_200_OK)
