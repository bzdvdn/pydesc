from django.db import models
from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager
	)
from departments.models import Subdivision, Department

class AcountManager(BaseUserManager):
	def create_user(self, email, name, last_name=None, password=None, is_active=True,  is_staff=False, is_admin=False):
		if not email:
			raise ValueError("Введите Email")
		if not password:
			raise ValueError("Введите пароль!")

		user_obj = self.model(email = self.normalize_email(email), name=name)

		user_obj.set_password(password) # changeuser password
		user_obj.staff = is_staff
		user_obj.admin = is_admin
		user_obj.active = is_active
		user_obj.save(using=self._db)

		return user_obj

	def create_staffuser(self, email, name, password=None):
		user = self.create_user(email, name, password=password, is_staff=True)
		return user

	def create_superuser(self, email, name, password=None):
		user = self.create_user(email, name, password=password, is_staff=True, is_admin=True)

		return user


class Account(AbstractBaseUser):
	email 		= models.EmailField(max_length=254, verbose_name="Email:", unique=True)
	name  		= models.CharField(max_length=255, blank=True, null=True, default="", verbose_name="Имя:")
	last_name 	= models.CharField(max_length=255, blank=True, null=True, default="", verbose_name = "Фамилия:")
	city = models.CharField(max_length=255, blank=True, null=True, default="", verbose_name="Город:")

	is_director = models.BooleanField(default=False, verbose_name='Директор:')
	is_chief = models.BooleanField(default=False, verbose_name="Начальник отдела:")
	is_substitute_chief = models.BooleanField(default=False, verbose_name="Зам,Начальник отдела:")


	active 		= models.BooleanField(default=True, verbose_name='Активен') # может логиниться

	staff 		= models.BooleanField(default=False, verbose_name='Сотрудник') # сотрудник не суперпользователь
	admin 		= models.BooleanField(default=False, verbose_name='Администратор') # суперпользователь
	timestamp 	= models.DateTimeField(auto_now_add=True, auto_now=False)

	EMAIL_FIELD = 'email'
	USERNAME_FIELD = 'email' #usename
	#USERNAME_FIELD and password are requiared by default
	REQUIRED_FIELDS = ['name']

	objects = AcountManager()

	class Meta:
		verbose_name = "Аккаунт"
		verbose_name_plural = "Аккаунты"
	

	def __str__(self):
		return f'{self.email}: {self.name}_{self.last_name}'

	def get_full_name(self):
		return f"{self.name}_{self.last_name}"

	def get_name(self):
		return self.name

	def get_email(self):
		return self.email

	def get_id(self):
		return self.pk

	def get_short_name(self):
		return self.name

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	@property
	def is_staff(self):
		return self.staff

	@property
	def is_admin(self):
		return self.admin

	@property
	def is_superuser(self):
		return self.admin

	@property
	def is_active(self):
		return self.active