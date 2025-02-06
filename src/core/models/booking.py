from src.core.models.base import *


class Booking(BaseModel):
    """Bron lar"""
    stadion = models.ForeignKey("Stadion", on_delete=models.CASCADE, related_name="bookings")
    booking_start_date = models.DateTimeField()
    booking_end_date = models.DateTimeField()

    class Meta:
        db_table = "bookings"

    def __str__(self):
        return f"{self.created_by.username}'s booking"
