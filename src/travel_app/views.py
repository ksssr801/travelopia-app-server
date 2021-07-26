from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import BookingDetailsSerializers
from .models import BookingDetails
from .utils.default_config import *
import time

class TravelAppViewSet(viewsets.ModelViewSet):
    serializer_class = BookingDetailsSerializers

    def get_queryset(self):
        return BookingDetails.objects.all()

    @action(detail=False, methods=['post'], name="do_booking", url_path='do-booking')
    def save_booking_info(self, request):
        try:
            data_obj = request.data
            booking_details_obj = BookingDetails()
            booking_details_obj.traveller = data_obj.get("traveller", '')
            booking_details_obj.email_id = data_obj.get("email", '')
            booking_details_obj.destination = int(data_obj.get("destination", ''))
            booking_details_obj.total_travellers = int(data_obj.get("travellersCount", ''))
            booking_details_obj.budget_per_person = int(data_obj.get("budget", ''))
            booking_details_obj.creation_time = int(time.time())
            booking_details_obj.last_update_time = int(time.time())
            try:
                booking_details_obj.save()
            except Exception as err:
                print ("Failed to save the booking details - %s - %s" % (type(err), err))
                return Response({"status": "failed"}, status=status.HTTP_501_NOT_IMPLEMENTED)
            return Response({"status": "success"}, status=status.HTTP_200_OK)
        except Exception as err:
            print ("Error in saving the booking details - %s - %s" % (type(err), err))
            return Response({"status": "error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['get'], name="booking_details", url_path='booking-details')
    def get_booking_details(self, request):
        try:
            print ("request : ", request.GET)
            all_booking_details = BookingDetails.objects.filter(is_deleted=False).order_by('-creation_time')
            serialized_data = BookingDetailsSerializers(all_booking_details, many=True).data
            destination_id_val_map = {ob.get('id', ''): ob.get('name', '') for ob in DESTINATION_LIST}
            for data in serialized_data: data.update({'destination': destination_id_val_map.get(data.get('destination', None)), 'readable_creation_time': time.ctime(data.get('creation_time'))})
            return Response(serialized_data, status=status.HTTP_200_OK)
        except Exception as err:
            print ("Error in fetching the booking details. - %s - %s" % (type(err), err))
            return Response({"status": "error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['get'], name="option_config", url_path='option-config')
    def get_init_option_config(self, request):
        try:
            default_option = {}
            default_option.update({
                'destination_list': DESTINATION_LIST,
            })
            return Response(default_option, status=status.HTTP_200_OK)
        except Exception as err:
            print ("Error in fetching the default options.")
            return Response({'status': 'error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
