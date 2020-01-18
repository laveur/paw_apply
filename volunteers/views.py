import datetime
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Department, DaysAvailable, Event, TimesAvailable, Volunteer

# Create your views here.
def index(request):
    context = {'is_volunteers': True}
    return render(request, 'volunteers.html', context)

def apply(request):
    event = Event.objects.get(event_end__gte=datetime.date.today())
    departments = Department.objects.all()
    days = DaysAvailable.objects.all()
    times = TimesAvailable.objects.all()
    context = {
        'is_volunteers': True,
        'event': event,
        'departments': departments,
        'days': days,
        'times': times,
    }
    return render(request, 'volunteer-apply.html', context)

def new(request):
    try:
        # Event
        event = Event.objects.get(pk=request.POST['event'])

        # Departments
        departments = Department.objects.filter(id__in=request.POST.getlist('department'))

        # Days available
        days = DaysAvailable.objects.filter(key__in=request.POST.getlist('days'))

        # Times available
        times = TimesAvailable.objects.filter(key__in=request.POST.getlist('times'))
    except (KeyError, Event.DoesNotExist, Department.DoesNotExist, DaysAvailable.DoesNotExist, TimesAvailable.DoesNotExist):
        event = Event.objects.get(event_end__gte=datetime.date.today())
        departments = Department.objects.all()
        days = DaysAvailable.objects.all()
        times = TimesAvailable.objects.all()
        context = {
            'is_volunteers': True,
            'event': event,
            'departments': departments,
            'days': days,
            'times': times,
            'error': 'Something has gone wrong, please contact us at <a href="mailto:feedback@pacanthro.org" class="alert-link">feedback@pacanthro.org</a>'
        }
        return render(request, 'volunteer-apply.html', context)
    else:
        volunteer = Volunteer()
        volunteer.event = event
        volunteer.email = request.POST['email']
        volunteer.legal_name = request.POST['legal_name']
        volunteer.fan_name = request.POST['fan_name']
        volunteer.phone_number = request.POST['phone']
        volunteer.twitter_handle = request.POST['twitter']
        volunteer.telegram_handle = request.POST['telegram']
        volunteer.volunteer_history = request.POST['history']
        volunteer.special_skills = request.POST['skills']
        volunteer.avail_setup = request.POST.get('setup', default=False)
        volunteer.avail_teardown = request.POST.get('teardown',default=False)

        try:
            volunteer.save()
        except (IntegrityError):
            event = Event.objects.get(event_end__gte=datetime.date.today())
            departments = Department.objects.all()
            days = DaysAvailable.objects.all()
            times = TimesAvailable.objects.all()
            context = {
                'is_volunteers': True,
                'event': event,
                'departments': departments,
                'days': days,
                'times': times,
                'error': 'Email has already applied.'
            }
            return render(request, 'volunteer-apply.html', context)

        for department in departments:
            volunteer.department_interest.add(department)

        for day in days:
            volunteer.days_available.add(day)

        for time in times:
            volunteer.time_availble.add(time)

        context = {
            'is_volunteers': True
        }
        return HttpResponseRedirect(reverse('volunteers:confirm'))

def confirm(request):
    return render(request, 'volunteer-confirm.html', {'is_volunteers': True})
