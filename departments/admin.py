from django.contrib import admin
from .models import Subdivision, Department


class SubdivisionAdmin(admin.ModelAdmin):
	list_display = ["name", "city"]
	list_filter = ["city"]
	search_fields = ('name',)

	class Meta:
		model = Subdivision

admin.site.register(Subdivision, SubdivisionAdmin)

class DepartmentAdmin(admin.ModelAdmin):
	list_display = ["name", "subdivision", "chief", "substitute_chief"]
	list_filter = ["subdivision"]
	search_fields = ('name',"subdivision", "chief")

	class Meta:
		model = Department

admin.site.register(Department, DepartmentAdmin)
