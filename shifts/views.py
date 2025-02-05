from django.shortcuts import render
from .models import EmployeeAllocation

def employee_allocation_by_shift(request, shift):
    # Fetch employee allocations filtered by shift
    allocations = EmployeeAllocation.objects.filter(employee__shift__name=shift)

    context = {
        'shift': shift,
        'allocations': allocations
    }

    return render(request, 'shifts/employee_allocation_by_shift.html', context)
