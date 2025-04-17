from django.urls import path
from . import views as accountViews

urlpatterns = [
    path('signupaccount/', accountViews.signupaccount, name="signupaccount"),
    path('loginaccount/', accountViews.loginaccount, name="loginaccount"),
    path('logoutaccount/', accountViews.logoutaccount, name="logoutaccount"),
]