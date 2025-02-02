import os
import django
from datetime import timedelta, date
from shifts.models import Shift, ShiftPattern

# Set up Django environment (only needed when running as a script)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "labour_management.settings")
django.setup()

def generate_shift_patterns(days_to_generate=365):
    """
    Generates shift patterns beyond the last available shift pattern date.
    If no shift pattern exists, starts from the predefined initial shift start date.
    """
    shifts = {shift.name: shift for shift in Shift.objects.all()}
    
    # 🚀 Step 1: Get the last recorded date from ShiftPattern
    last_shift = ShiftPattern.objects.order_by("-date").first()
    
    # 🚀 Step 2: Decide where to start generating shifts
    if last_shift:
        start_date = last_shift.date + timedelta(days=1)
    else:
        start_date = date(2024, 12, 29)  # Initial start date

    end_date = start_date + timedelta(days=days_to_generate)
    
    print(f"✅ Generating shift patterns from {start_date} to {end_date}")

    # 🚀 Step 3: Generate shifts in a rolling cycle
    current_date = start_date
    while current_date <= end_date:
        for shift in shifts.values():
            shift_type = shift.get_shift_type(current_date)  # Determine shift type

            # Only create ShiftPattern if not "Off"
            if shift_type != "Off":
                ShiftPattern.objects.create(
                    shift=shift,
                    date=current_date,
                    shift_type=shift_type
                )
                print(f"✅ Assigned {shift.name} ({shift_type}) on {current_date}")

        current_date += timedelta(days=1)

    print("✅ Shift pattern successfully updated!")

if __name__ == "__main__":
    generate_shift_patterns(365)  # Generate 1 year ahead
