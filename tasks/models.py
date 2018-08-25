from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings

from departments.models import Subdivision, Department


class Document(models.Model):
	name = models.CharField(max_length=255, blank=True, null=True, default="", verbose_name="Название:")
	description = models.CharField(max_length=1024, blank=True, null=True, default="", verbose_name="Описание:")
	filepath = models.FileField(upload_to='media/documents/', max_length=500, default=None, verbose_name="Файл:")
	order = models.BooleanField(default=False, verbose_name="Приказ")

	class Meta:
		verbose_name = "Документ"
		verbose_name = "Документы"

	def __str__(self):
		return self.name

	@property
	def is_order(self):
		return self.order

class MainTask(models.Model):
	name = models.CharField(max_length=255, verbose_name="Название:")
	description = RichTextUploadingField(blank=True, null=True, default=None,  max_length=8000, verbose_name = 'Описание:')
	document = models.OneToOneField(Document, blank=True, null=True, default=None, verbose_name="Приклипленные документ:", related_name="main_task_document", on_delete=models.CASCADE)

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
	document = models.OneToOneField(Document, blank=True, null=True, default=None, verbose_name="Приклипленные документ:", related_name="task_document", on_delete=models.CASCADE)
	department = models.ForeignKey(Department, blank=True, null=True, default=None, on_delete=models.CASCADE, related_name="task_department")
	watchers = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True, default=None, verbose_name="Наблюдатели", related_name="task_watchers")
	executor = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, default=None, verbose_name="Исполнитель", on_delete=models.CASCADE, related_name="task_executor")
	deadline = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Срок До:")
	closed = models.BooleanField(default=False, verbose_name="Закрыта:")
	closetime = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Закрыта в:")

	class Meta:
		verbose_name = 'Задача'
		verbose_name_plural = 'Задачи'

	def __str__(self):
		return self.name

	@property
	def get_executor(self):
		return self.executor.name

	@property
	def get_watchers(self):
		return self.watchers

	@property
	def get_department(self):
		return self.department.name

	@property
	def is_closed(self):
		return self.closed


class TaskTimestamp(models.Model):
	task = models.ForeignKey(Task, verbose_name="задача", on_delete=models.CASCADE, related_name="task_timestamp")
	time = 	models.IntegerField(default=0, verbose_name="Потрачено времени в сек.")

	class Meta:
		verbose_name = "Время на задачу"
		verbose_name_plural = "Задачи и время потраченное на них"

	def __str__(self):
		return f"{self.task.main_task.name} - {self.task.name}"

	@property
	def get_taks_name(self):
		return self.task.name