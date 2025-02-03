from django.db import models
from datetime import timedelta

#Shift model
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

#Shift pattern model
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

# Work Area Model
class WorkArea(models.Model):
    TASK_CHOICES = [
        ('Operational', 'Operational'),
        ('Overhead', 'Overhead'),
    ]

    LINE_CHOICES = [
        ('1', 'Line 1'),
        ('2', 'Line 2'),
        ('3', 'Line 3'),
        ('4', 'Line 4'),
        ('MOH', 'Manufacturing Overhead (MOH)'),
        ('Shared', 'Shared Resources'),
    ]

    line = models.CharField(
        max_length=10, 
        choices=LINE_CHOICES, 
        help_text="Select the production line or work area category"
    )
    name = models.CharField(
        max_length=50, 
        help_text="Name of the work area (e.g., Process, Multipack, Palletiser)"
    )
    subwork_area = models.CharField(
        max_length=50, 
        help_text="Specific task area (e.g., Fryer Operator, Zone Runner)"
    )
    required_employees = models.PositiveIntegerField(
        default=1, 
        help_text="Number of employees required for this work area"
    )
    employee_type = models.CharField(
        max_length=50, 
        help_text="Type of employee needed (e.g., General Operator, Manufacturing Technician)"
    )
    task_type = models.CharField(
        max_length=20, 
        choices=TASK_CHOICES, 
        help_text="Defines if the task is Operational or Overhead"
    )

    def __str__(self):
        return f"Line {self.line} - {self.name} - {self.subwork_area}"

