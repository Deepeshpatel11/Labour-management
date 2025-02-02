from django.db import models
from datetime import timedelta

class Shift(models.Model):
    SHIFT_CHOICES = [
        ('Red', 'Red Shift'),
        ('Green', 'Green Shift'),
        ('Blue', 'Blue Shift'),
        ('Yellow', 'Yellow Shift'),
    ]

    name = models.CharField(max_length=10, choices=SHIFT_CHOICES, unique=True)
    start_date = models.DateField(help_text="The date when this shift starts")
    cycle_length = models.PositiveIntegerField(default=16, help_text="Length of the shift cycle in days")

    def __str__(self):
        return f"{self.name}"


class ShiftPattern(models.Model):
    SHIFT_TYPE_CHOICES = [
        ('Day', 'Day Shift'),
        ('Night', 'Night Shift'),
        ('Off', 'Off'),
    ]

    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    date = models.DateField(help_text="The actual date of this shift")
    shift_type = models.CharField(max_length=10, choices=SHIFT_TYPE_CHOICES)

    class Meta:
        unique_together = ('shift', 'date')  # Ensures no duplicate shift records

    def __str__(self):
        return f"{self.shift.name} - {self.shift_type} - {self.date}"
