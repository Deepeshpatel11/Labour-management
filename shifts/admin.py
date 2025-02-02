from django.contrib import admin
from .models import Shift, ShiftPattern

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
