from django.urls import path
from .views import employee_allocation_by_shift

urlpatterns = [
    path('allocations/<str:shift>/', employee_allocation_by_shift, name='employee_allocation_by_shift'),
]
