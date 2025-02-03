from django.db import models

class Employee(models.Model):
    EMPLOYEE_ROLES = [
        ('Shift Technician', 'Shift Technician'),
        ('Manufacturing Technician', 'Manufacturing Technician'),
        ('General Operator', 'General Operator'),
        ('General Support Operator', 'General Support Operator'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    employee_id = models.CharField(max_length=10, unique=True, help_text="Unique ID for the employee")
    role = models.CharField(max_length=50, choices=EMPLOYEE_ROLES)
    date_joined = models.DateField(help_text="Date the employee joined the company")

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role})"
