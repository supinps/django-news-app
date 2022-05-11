from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import PortalUser

# Form to be used in rendering custom user model **PortalUser** in the admin panel
# the custom user model **PortalUser** adds additional fields to implement business logic
# this forms.py will be imported to admin.py in the users app
#Two forms are defined for user creation and user change

class PortalUserCreationForm(UserCreationForm):

    class Meta:
        model = PortalUser
        fields = ('username', 'email', 'first_name', 'last_name')

class PortalUserChangeForm(UserChangeForm):

    class Meta:
        model = PortalUser
        fields = ('username', 'email', 'first_name', 'last_name')
