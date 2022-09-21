from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .forms import UserCreationForm, UserChangeForm
from .models import User



class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username', 'email', 'is_active', 'is_admin')
    list_filter = ('is_active',)
    fieldsets = (
        ('Main', {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_admin', 'last_login')}),
    )

    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'password1', 'password2')}),
    )

    search_fields = ('username', 'email')
    ordering = ('date_joined',)
    filter_horizontal = ()


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
