from django.contrib import admin
from .models import Shift, ShiftPattern

@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ('name', 'shift_type', 'rotation_pattern')
    list_filter = ('shift_type',)

@admin.register(ShiftPattern)
class ShiftPatternAdmin(admin.ModelAdmin):
    list_display = ('shift', 'start_date', 'end_date')
    list_filter = ('shift',)
