from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()

class UserAdmin(BaseUserAdmin):
	form = UserAdminChangeForm
	add_form = UserAdminCreationForm

	list_display = ('email','name', 'admin',)
	list_filter = (
		'admin',
		'staff',
		'active',
		'is_chief',
		'is_substitute_chief',
		'is_director',
	)
	fieldsets = (
		(None, {'fields': ('name','last_name','city', 'email', 'password')}),
	    ('Полное имя', {'fields': ('name','last_name')}),
		('Статус', {'fields': (
			'admin',
			'staff',
			'active',
			'is_chief',
			'is_substitute_chief',
			'is_director'
			)
		}),
	)

	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'password1', 'password2')}
		),
	)
	search_fields = ('email', 'name',)
	ordering = ('email',)
	filter_horizontal = ()


admin.site.register(User, UserAdmin)

admin.site.unregister(Group)
