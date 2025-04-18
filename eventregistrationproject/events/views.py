from django.shortcuts import render, redirect
from .models import Events, Registrations
from .forms import EventForm
from django.contrib import messages
from django.utils import timezone

# Create your views here.
def events(request):
    if not request.user.is_authenticated:
        return redirect('loginaccount')
    registered_ids = set()
    upcoming_events = Events.objects.filter(start_date__gt=timezone.now())
    events = Events.objects.all()
    if request.user.groups.filter(name="Administrator").exists():
        is_admin = True
        registered_events = []
    else:
        is_admin = False
        registered_events = Registrations.objects.filter(user=request.user)
        registered_ids = {registration.event.id for registration in registered_events}

    return render(request, 'events.html', {'events': events, 'upcoming_events': upcoming_events, 'is_admin': is_admin, 'registered_ids': registered_ids, 'registered_events': registered_events})
    
def manage_event(request, event_id=None):
    if not request.user.is_authenticated:
        return redirect('loginaccount')
    if not request.user.groups.filter(name="Administrator").exists():
        messages.error(request, "You do not have permissions to view this page.")
        return redirect('events')
    if request.method == "GET":
        if event_id:
            event = Events.objects.get(pk=event_id)
            form = EventForm(instance=event)
        else:
            form = EventForm()
        return render(request, 'event_manage.html', {'form': form})
    elif request.method == "POST":
        if event_id:
            event = Events.objects.get(pk=event_id)
            form = EventForm(request.POST, instance=event)
        else:
            form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events')
        return render(request, 'event_manage.html', {'form': form, 'event_id': event_id})

def delete_event(request, event_id):
    if not request.user.is_authenticated:
        return redirect('loginaccount')
    if not request.user.groups.filter(name="Administrator").exists():
        messages.error(request, "You do not have permissions to view this page.")
        return redirect('events')
    event = Events.objects.get(pk=event_id)
    if request.method == "GET":
        return render(request, 'delete_event.html', {'event': event})
    elif request.method == "POST":
        event.delete()
        return redirect('events')
    
def register_event(request, event_id):
    if not request.user.is_authenticated:
        return redirect('loginaccount')
    if not request.user.groups.filter(name="Registrant").exists():
        messages.error(request, "You do not have permissions to view this page.")
        return redirect('events')
    event = Events.objects.get(pk=event_id)
    if Registrations.objects.filter(user=request.user, event=event).exists():
        messages.error(request, "You are already registered for this event.")
    else:
        Registrations.objects.create(user=request.user, event=event)
        messages.success(request, "You have successfully registered for the event.")
    return redirect('events') 

def unregister_event(request, event_id):
    if not request.user.is_authenticated:
        return redirect('loginaccount')
    if not request.user.groups.filter(name="Registrant").exists():
        messages.error(request, "You do not have permissions to view this page.")
        return redirect('events')
    event = Events.objects.get(pk=event_id)
    registration = Registrations.objects.filter(user=request.user, event=event).first()
    if registration:
        registration.delete()
        messages.success(request, "You have successfully unregistered from the event.")
    else:
        messages.error(request, "You are not registered for this event.")
    return redirect('events')
