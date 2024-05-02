from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserAdminCreationForm, CustomUserAdminChangeForm
admin.site.unregister(Group)
CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
	# The forms to add and change user instances
	model = CustomUser
	form = CustomUserAdminChangeForm   #update view
	add_form = CustomUserAdminCreationForm # create view

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
	list_display = ('email', 'username', 'is_superuser',)
	list_filter = ('is_superuser', 'is_staff', 'is_active',)
	fieldsets = (
		(None, {
			'fields': ('email', 'password',)
			}),
		('Username', {
			'fields': ('username',)
			}),
		('Permissions', {
			'fields': ('is_superuser', 'is_staff', 'is_active',)
			}),
		)
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'username', 'password', 'password_2', 'is_active', 'is_staff')}
			),
		)
	search_fields = ('email', 'username',)
	ordering = ('-date_joined',)
	filter_horizontal = ()

admin.site.register(CustomUser, CustomUserAdmin)
		
