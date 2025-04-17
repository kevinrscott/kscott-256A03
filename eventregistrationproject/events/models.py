from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Events(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return f"{self.name}"

class Registrations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    events = models.ManyToManyField(Events, related_name='registrants')

    def __str__(self):
        return f"{self.user.username} registered for events"