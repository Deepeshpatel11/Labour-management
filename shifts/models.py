from django.db import models

class Shift(models.Model):
    SHIFT_CHOICES = [
        ('Red', 'Red Shift'),
        ('Green', 'Green Shift'),
        ('Blue', 'Blue Shift'),
        ('Yellow', 'Yellow Shift'),
    ]

    SHIFT_TYPE_CHOICES = [
        ('Day', 'Day Shift'),
        ('Night', 'Night Shift'),
    ]

    name = models.CharField(max_length=10, choices=SHIFT_CHOICES, unique=True)
    shift_type = models.CharField(max_length=10, choices=SHIFT_TYPE_CHOICES)
    rotation_pattern = models.CharField(max_length=20, default="4 on, 4 off")

    def __str__(self):
        return f"{self.name} ({self.shift_type})"

class ShiftPattern(models.Model):
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.shift} from {self.start_date} to {self.end_date}"
