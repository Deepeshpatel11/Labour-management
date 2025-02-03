from django.contrib import admin
from .models import Employee  # Import Employee model

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'employee_id', 'role', 'shift')  # Added shift
    list_filter = ('role', 'shift')  # Allow filtering by shift
    search_fields = ('first_name', 'last_name', 'employee_id')
    ordering = ('first_name', 'last_name')
