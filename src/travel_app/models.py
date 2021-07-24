from django.db import models

class BookingDetails(models.Model):
    booking_id = models.IntegerField(primary_key=True)
    traveller = models.CharField(max_length=254)
    email_id = models.EmailField(max_length=254)
    destination = models.IntegerField()
    total_travellers = models.IntegerField()
    budget_per_person = models.IntegerField()

    class Meta:
        db_table = 'tbl_booking_details'