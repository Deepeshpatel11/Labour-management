from django.db import models

class Shift(models.Model):
    SHIFT_CHOICES = [
        ('Red', 'Red Shift'),
        ('Green', 'Green Shift'),
        ('Blue', 'Blue Shift'),
        ('Yellow', 'Yellow Shift'),
    ]

    name = models.CharField(max_length=10, choices=SHIFT_CHOICES, unique=True)
    shift_type = models.CharField(max_length=5, choices=[('Day', 'Day'), ('Night', 'Night')])
    rotation_pattern = models.TextField(help_text="Describe the shift rotation pattern")

    def __str__(self):
        return f"{self.name} - {self.shift_type}"
