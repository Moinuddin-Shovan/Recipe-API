from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUser
from core import models
from django.utils.translation import gettext as _


class UserAdmin(BaseUser):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
        # Comma here is important. Not to confuse it as an object
    )


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Tag)
