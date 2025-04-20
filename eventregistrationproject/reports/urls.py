from django.urls import path
from . import views as reportViews

urlpatterns = [
    path('users/', reportViews.users, name='users'),
    path('registrants/', reportViews.registrants, name='registrants'),
]