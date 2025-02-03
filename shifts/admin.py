from django.contrib import admin
from .models import Shift, ShiftPattern, WorkArea, EmployeeAllocation

@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'cycle_length')
    ordering = ('start_date',)
    search_fields = ('name',)

@admin.register(ShiftPattern)
class ShiftPatternAdmin(admin.ModelAdmin):
    list_display = ('shift', 'date', 'shift_type')
    list_filter = ('shift', 'shift_type', 'date')
    ordering = ('date',)
    search_fields = ('shift__name', 'date')

@admin.register(WorkArea)
class WorkAreaAdmin(admin.ModelAdmin):
    list_display = ('line', 'name', 'subwork_area', 'required_employees', 'employee_type', 'task_type')
    list_filter = ('line', 'name', 'task_type')
    ordering = ('line', 'name')
    search_fields = ('name', 'subwork_area', 'employee_type')

@admin.register(EmployeeAllocation)
class EmployeeAllocationAdmin(admin.ModelAdmin):
    list_display = ('employee', 'work_area', 'shift_pattern')  # Fields to show in admin list view
    list_filter = ('work_area', 'shift_pattern')  # Filters for easier navigation
    search_fields = ('employee__first_name', 'employee__last_name', 'work_area__name')  # Search functionality
    ordering = ('shift_pattern', 'employee')  # Order by shift pattern and employee