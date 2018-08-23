from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings

from departments.models import Subdivision, Department


class MainTask(models.Model):
	name = models.CharField(max_length=255, verbose_name="Название:")
	description = RichTextUploadingField(blank=True, null=True, default=None,  max_length=8000, verbose_name = 'Описание:')

	class Meta:
		verbose_name = 'Цель(Главная задача)'
		verbose_name_plural = 'Цели(Главные задачи)'

	def __str__(self):
		return self.name


class Task(models.Model):
	name = models.CharField(max_length=255, verbose_name="Название:")
	main_task = models.ForeignKey(MainTask, blank=True, null=True, default=None, on_delete=models.CASCADE, related_name="main_task", verbose_name="Цель")
	description = RichTextUploadingField(blank=True, null=True, default=None,  max_length=8000,verbose_name = 'Описание:')
	subdivision = models.ForeignKey(Subdivision, verbose_name="Мое подрахделение:", blank=True, null=True, default=None, on_delete=models.CASCADE, related_name="task_sub")
	department = models.ForeignKey(Department, blank=True, null=True, default=None, on_delete=models.CASCADE, related_name="task_department")
	watchers = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True, default=None, verbose_name="Наблюдатели", related_name="task_watchers")
	executor = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, default=None, verbose_name="Исполнитель", on_delete=models.CASCADE, related_name="task_executor")
	deadline = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Срок До:")
	closetime = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Завершена в:")

	class Meta:
		verbose_name = 'Задача'
		verbose_name_plural = 'Задачи'

	def __str__(self):
		return self.name


class TaskTimestamp(models.Model):
	task = models.ForeignKey(Task, verbose_name="задача", on_delete=models.CASCADE, related_name="task_timestamp")
	time = 	models.IntegerField(default=0, verbose_name="Потрачено времени в сек.")

	class Meta:
		verbose_name = "Время на задачу"
		verbose_name_plural = "Задачи и время потраченное на них"

	def __str__(self):
		return f"{self.task.main_task.name} - {self.task.name}"
