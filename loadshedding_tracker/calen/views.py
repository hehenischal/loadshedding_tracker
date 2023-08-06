from django.shortcuts import render
import calendar
from django.utils import timezone
from .models import Outage
from .forms import OutageForm

def calendar_view(request):
    year = int(request.GET.get('year', timezone.now().year))
    month = int(request.GET.get('month', timezone.now().month))
    ward_number = int(request.GET.get('ward', 0))

    # Get the first day of the month and the last day of the month
    first_day = timezone.datetime(year, month, 1)
    last_day = timezone.datetime(year, month, calendar.monthrange(year, month)[1])

    # Get the day of the week for the first day of the month
    start_day = first_day.weekday()

    # Calculate the days for the calendar
    cal = []
    week = [0] * start_day
    for day in range(1, last_day.day + 1):
        week.append(day)
        if len(week) == 7:
            cal.append(week)
            week = []
    if week:
        # Add empty cells for the next month
        week += [0] * (7 - len(week))
        cal.append(week)

    # Process outage form submission
    if request.method == 'POST':
        ward_number = request.POST.get('ward_number')
    if int(ward_number) > 0:
        outages = Outage.objects.filter(ward_number=ward_number)
        ward_outages = [outage.date.day for outage in outages]
        print("ward_outages")
        for outage in ward_outages:
            print(outage)
    else:
        ward_outages = []

    context = {
        'year': year,
        'month': month,
        'calendar': cal,
        'ward_number': ward_number,
        'ward_outages': ward_outages,
        'form': OutageForm(),
    }

    return render(request, 'index.html', context)
