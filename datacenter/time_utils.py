from django.utils.timezone import localtime
from datetime import timedelta


def get_duration(entered_at, leaved_at=None):
    entered_time = localtime(entered_at)
    if leaved_at:
        leaved_time = localtime(leaved_at)
        duration = leaved_time - entered_time
    else:
        current_time = localtime()
        duration = current_time - entered_time
    return duration


def format_duration(duration):
    hours, remainder = divmod(duration.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    return f'{hours} часов {minutes} минут'
