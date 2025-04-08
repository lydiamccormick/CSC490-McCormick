from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class CreateAccount(UserCreationForm):
    email = forms.EmailField()
    def __init__(self, *args, **kwargs):
        super(CreateAccount, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class SignIn(AuthenticationForm):
    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)

