from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import PortalUserCreationForm, PortalUserChangeForm
from .models import PortalUser

# Custom user models need to be registered in the admin app, so these models can be accessed from admin dashboard
# list_display defines the rendering of database in the dashboard

class PortalUserAdmin(UserAdmin):
    add_form = PortalUserCreationForm
    form = PortalUserChangeForm
    model = PortalUser
    list_display = ['email', 'username', 'is_author', 'is_editor']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'is_author', 'is_editor', 'password1', 'password2')}
        ),
    )

admin.site.register(PortalUser, PortalUserAdmin)
