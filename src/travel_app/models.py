from django.db import models

class BookingDetails(models.Model):
    booking_id = models.AutoField(primary_key=True)
    traveller = models.CharField(max_length=254)
    email_id = models.EmailField(max_length=254)
    destination = models.IntegerField(null=True)
    total_travellers = models.IntegerField(null=True)
    budget_per_person = models.IntegerField(null=True)
    last_update_time = models.IntegerField(null=True)
    creation_time = models.IntegerField(null=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'tbl_booking_details'