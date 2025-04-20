"""
URL configuration for eventregistration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from events import views as eventViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('reports/', include('reports.urls')),
    path('', eventViews.events, name='events'),
    path('event/create/', eventViews.manage_event, name='create_event'),
    path('event/update/<int:event_id>/', eventViews.manage_event, name='update_event'),
    path('event/delete/<int:event_id>/', eventViews.delete_event, name='delete_event'),
    path('event/register/<int:event_id>/', eventViews.register_event, name='register_event'),
    path('event/unregister/<int:event_id>/', eventViews.unregister_event, name='unregister_event'),
]
