from django.db import models
from shifts.models import Shift  # Import Shift model

class Employee(models.Model):
    ROLE_CHOICES = [
        ('Shift Technician', 'Shift Technician'),
        ('Manufacturing Technician', 'Manufacturing Technician'),
        ('General Operator', 'General Operator'),
        ('General Support Operator', 'General Support Operator'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    employee_id = models.CharField(max_length=10, unique=True, help_text="Unique Employee ID")
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, help_text="Employee Role")
    shift = models.ForeignKey(Shift, on_delete=models.SET_NULL, null=True, blank=True, help_text="Default assigned shift")

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.role}"
