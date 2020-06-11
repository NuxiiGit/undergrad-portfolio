from django.conf import settings
from django.db import models
from django.core import validators

class Contact(models.Model):
	email = models.EmailField(max_length=70)
	phone = models.CharField(max_length=16, validators=[validators.RegexValidator(r'\+(\d+)')])
	website = models.URLField(default='')

	def publish(self):
		self.save()

	def __str__(self):
		return self.email

class Skill(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()

	def publish(self):
		self.save()

	def __str__(self):
		return self.title

class Experience(models.Model):
	start_date = models.DateTimeField(blank=True, null=True)
	start_end = models.DateTimeField(blank=True, null=True)
	employer = models.CharField(max_length=200)
	position = models.CharField(max_length=200)
	description = models.TextField()

	def publish(self):
		self.save()

	def __str__(self):
		return self.position

class Education(models.Model):
	start_date = models.DateTimeField(blank=True, null=True)
	start_end = models.DateTimeField(blank=True, null=True)
	degree = models.CharField(max_length=200)
	subject = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	country = models.CharField(max_length=200)

	def publish(self):
		self.save()

	def __str__(self):
		return self.subject