from django.db import models
from django.contrib.auth.models import User

# from dashboard import helper


class Operator(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	role = models.ForeignKey("Role", on_delete=models.CASCADE)
	api_pass = models.CharField(max_length=256, default="pass")
	api_token = models.CharField(max_length=25, unique=True, blank=True)
	phone_number = models.CharField(max_length=13, unique=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)

	def describe_name(self):
		return self.user.first_name + " " + self.user.last_name

	def save(self, *arg, **kwrg):
		# encrypt api_pass before saving
		from .helper import Encrypt_Decrypt
		self.api_pass = Encrypt_Decrypt().encrypt(self.user.username, self.api_pass)
		super(Operator, self).save(*arg, **kwrg)

	def __str__(self):
		return self.describe_name() + "--" + self.role

class Role(models.Model):
	designation = models.CharField(max_length=30)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.designation