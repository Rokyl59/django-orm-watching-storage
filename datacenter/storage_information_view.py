import os
import django
from django.shortcuts import render
from django.utils.timezone import localtime, now
from datetime import timedelta
from datacenter.models import Visit

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()


def get_duration(entered_at):
    entered_time = localtime(entered_at)
    current_time = localtime(now())
    duration = current_time - entered_time
    return str(timedelta(seconds=duration.total_seconds()))[:-3]


def format_duration(duration_str):
    hours, minutes, _ = duration_str.split(':')
    return f'{hours} часов {minutes} минут'


def storage_information_view(request):
    active_visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []

    for visit in active_visits:
        entered_at = visit.entered_at
        duration = get_duration(entered_at)
        formatted_duration = format_duration(duration)
        non_closed_visits.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': localtime(entered_at).strftime("%d-%m-%Y %H:%M:%S"),
            'duration': formatted_duration,
        })

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
