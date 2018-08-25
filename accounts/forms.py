from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = get_user_model()

class UserAdminCreationForm(forms.ModelForm):
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('name', 'email',)

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")

		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")
		return password2

	def save(self, commit=True):
		user = super(UserAdminCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])

		if commit:
			user.save()
		return user



class UserAdminChangeForm(forms.ModelForm):
	password = ReadOnlyPasswordHashField()

	class Meta:
		model = User
		fields = (
			'name',
			'last_name',
			'email',
			'city',
			'password',
			'active',
			'admin',
			'is_chief',
			'is_substitute_chief',
			'is_director'
		)

	def clean_password(self):
		return self.initial["password"]

class LoginForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)



class RegisterForm(forms.ModelForm):
	password1 = forms.CharField()
	password2 = forms.CharField()


	class Meta:
		model = User
		fields = ('name', 'email',)

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")
		return password2


	def save(self, commit=True):
		user = super(RegisterForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		#user.active = False # send email confirm
		if commit:
			user.save()
		return user


class UserChangeInfoForm(forms.Form):
	email = forms.EmailField(required=False)
	name =forms.CharField(required=False)
	last_name = forms.CharField(required=False)
	city = forms.CharField(required=False)


class UserChangePasswordForm(forms.Form):
	password1 = forms.CharField()
	password2 = forms.CharField()

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")
		return password2


	

