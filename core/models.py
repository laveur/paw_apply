import datetime
from django.db import models

def get_current_event():
    return Event.objects.filter(event_end__gte=datetime.date.today()).order_by('event_end').first()

# Create your models here.
class ApplicationState(models.TextChoices):
    STATE_NEW = "STATE_NEW", "New"
    STATE_ACCEPTED = "STATE_ACCEPTED", "Accepted"
    STATE_ASSIGNED = "STATE_ASSIGNED", "Assigned"
    STATE_WAITLIST = "STATE_WAITLIST", "Waitlisted"
    STATE_DENIED = "STATE_DENIED", "Denied"
    STATE_DELETED = "STATE_DELETED", "Deleted"
    STATE_OLD = "STATE_OLD", "Migrated Data"

class DaysAvailable(models.Model):
    key = models.CharField(max_length=4, primary_key=True)
    name = models.CharField(max_length=50)
    order = models.IntegerField(default=0)
    available_scheduling = models.BooleanField(default=False)
    available_party = models.BooleanField(default=False)
    party_only = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Department(models.Model):
    department_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.department_name

class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_start = models.DateField()
    event_end = models.DateField()
    max_merchants = models.IntegerField(default=0)
    max_party_rooms = models.IntegerField(default=0)
    submissions_end = models.DateField()

    def is_submissions_closed(self):
        return self.submissions_end < datetime.date.today()

    def __str__(self):
        return self.event_name
