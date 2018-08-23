from django.db import models
from django.conf import settings

# Create your models here.
class Subdivision(models.Model):
	name = models.CharField(max_length=255, blank=True, null=True, default="", verbose_name="Название:")
	city = models.CharField(max_length=255, blank=True, null=True, default="", verbose_name="Город:")
	description = models.CharField(max_length=1024, blank=True, null=True, default="", verbose_name="Описание:")

	class Meta:
		verbose_name = "Подраздиление"
		verbose_name_plural = "Подразделения"

	def __str__(self):
		return f"{self.name}: {self.city}"

class Department(models.Model):
	name = models.CharField(max_length=255, blank=True, null=True, default="", verbose_name="Название:")
	description = models.CharField(max_length=1024, blank=True, null=True, default="", verbose_name="Описание:")
	subdivision = models.ForeignKey(Subdivision, verbose_name="Мое подрахделение:", blank=True, null=True, default=None, on_delete=models.CASCADE, related_name="subs")
	chief = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True, null=True, default=None, verbose_name="Начальник отдела:", on_delete=models.CASCADE, related_name="account")
	substitute_chief = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True, null=True, default=None, verbose_name="Зам. Начальника отдела:", on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Отдел"
		verbose_name_plural = "Отделы"

	def __str__(self):
		return f"{self.name}: {self.chief}"