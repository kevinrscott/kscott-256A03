from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from events.models import Events, Registrations

# Create your views here.
def users(request):
    if not request.user.is_authenticated:
        return redirect('loginaccount')
    if not request.user.groups.filter(name="Administrator").exists():
        messages.error(request, "You do not have permissions to view this page.")
        return redirect('events')
    is_admin = True
    all_users = User.objects.all()
    user_info = []
    for user in all_users:
        full_name = user.first_name.title() + ' ' + user.last_name.title()
        role = user.groups.first().name if user.groups.exists() else 'No Role'
        user_info.append({
            'username': user.username,
            'full_name': full_name,
            'role': role,
        })
    return render(request, 'users.html', {'users': user_info, 'is_admin': is_admin})

def registrants(request):
    if not request.user.is_authenticated:
        return redirect('loginaccount')
    if not request.user.groups.filter(name="Administrator").exists():
        messages.error(request, "You do not have permissions to view this page.")
        return redirect('events')
    is_admin = True
    event_data = []
    
    for event in Events.objects.all():
        registrants = Registrations.objects.filter(event=event).select_related('user')
        event_data.append({
            'event': event,
            'registrants': registrants
        })
        
    return render(request, 'registrants.html', {'events': event_data, 'is_admin': is_admin})