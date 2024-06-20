from django.shortcuts import render
from profiles.models import Team, Rider, Event
import datetime

def home_view(request):
    teams = Team.objects.all()
    riders = Rider.objects.all()
    events = Event.objects.order_by('date').filter(date__gte=datetime.date.today())  # Upcoming events
    user = request.user
    context = {
        'teams': teams,
        'riders': riders,
        'events': events,
        "user": user 
    }
    
    return render(request, 'core/base.html', context)
