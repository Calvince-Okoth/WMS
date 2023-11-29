from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from WMS.models import wasterequest
from django.contrib.auth.forms import UserCreationForm


class wasterequestform(forms.ModelForm):
    class Meta:
        model=wasterequest
        fields='__all__'


class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

        def clean_password(self, username=None, cleaned_data=None):
            password = self.cleaned_data.get('password')

            # Your custom validation logic goes here
            if len(password) < 8:
                raise ValidationError('Password must be at least 8 characters long.')
            if username == 'example' and password == 'password':
                # If authentication is successful, set a custom message
                self.add_error('username', 'Login successful!')

            return cleaned_data

            return password


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        self.fields['username'].help_text = ''

