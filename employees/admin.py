from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'employee_id', 'role', 'date_joined')
    search_fields = ('first_name', 'last_name', 'employee_id', 'role')
    ordering = ('last_name',)
