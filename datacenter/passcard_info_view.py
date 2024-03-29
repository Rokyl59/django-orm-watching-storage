from django.shortcuts import render, get_object_or_404
from datacenter.models import Passcard, Visit
from datetime import timedelta
from django.utils.timezone import localtime
from django.http import Http404


def get_duration(entered_at, leaved_at):
    entered_time = localtime(entered_at)
    leaved_time = localtime(leaved_at)
    duration = leaved_time - entered_time
    return duration


def format_duration(duration):
    hours, remainder = divmod(duration.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    return f'{hours} часов {minutes} минут'


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    passcard_visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []
    for visit in passcard_visits:
        entered_at = visit.entered_at
        leaved_at = visit.leaved_at
        duration = get_duration(entered_at, leaved_at) if leaved_at else timedelta(0)
        is_strange = duration.total_seconds() > 3600
        this_passcard_visits.append({
            'entered_at': localtime(entered_at).strftime("%d-%m-%Y %H:%M:%S"),
            'duration': format_duration(duration),
            'is_strange': is_strange,
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits,
    }
    return render(request, 'passcard_info.html', context)
