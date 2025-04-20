from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class AuthenticateForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password']:
            self.fields[fieldname].widget.attrs.update({'class': 'mb-4 px-3 py-2 border border-gray-400 rounded-md w-full focus:outline-none focus:ring-2 focus:ring-blue-950"'})
            
class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2', 'first_name', 'last_name']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({'class': 'px-3 py-2 border border-gray-400 rounded-md w-full focus:outline-none focus:ring-2 focus:ring-blue-950"'})
            
    class Meta:   
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')