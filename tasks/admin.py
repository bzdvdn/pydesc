from django.contrib import admin
from .models import Task, MainTask

class MainTaskAdmin(admin.ModelAdmin):
	list_display = ["name", "description"]
	search_fields = ('name',)

	class Meta:
		model = MainTask


admin.site.register(MainTask, MainTaskAdmin)

class TaskAdmin(admin.ModelAdmin):
	list_display = [
		"name",
		"main_task",
		"subdivision",
		"department",
		"executor",
		"deadline",
		"closetime" 
	]
	list_filter = ["executor", "department", "main_task", "subdivision"]
	search_fields = ('name', "executor","main_task")

	class Meta:
		model = Task

admin.site.register(Task, TaskAdmin)