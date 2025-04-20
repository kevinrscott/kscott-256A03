from django import forms
from .models import Events
from django.utils.timezone import now

class EventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'mb-4 px-3 py-2 border border-gray-300 rounded-md w-full focus:outline-none focus:ring-2 focus:ring-blue-950'
            })
    class Meta:
        model = Events
        fields = ['name', 'description', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'min': now().date().isoformat()}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }