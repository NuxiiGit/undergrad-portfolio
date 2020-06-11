from django.conf import settings
from django.db import models
from django.core import validators

MAX_LENGTH = 255

class Contact(models.Model):
	email = models.EmailField(max_length=MAX_LENGTH)
	phone = models.CharField(max_length=16, validators=[validators.RegexValidator(r'\+(\d+)')])
	website = models.URLField(default='')

	def publish(self):
		self.save()

	def __str__(self):
		return self.email

class Skill(models.Model):
	title = models.CharField(max_length=MAX_LENGTH)
	description = models.TextField()

	def publish(self):
		self.save()

	def __str__(self):
		return self.title

class Experience(models.Model):
	start_date = models.DateTimeField(blank=True, null=True)
	start_end = models.DateTimeField(blank=True, null=True)
	employer = models.CharField(max_length=MAX_LENGTH)
	position = models.CharField(max_length=MAX_LENGTH)
	description = models.TextField()

	def publish(self):
		self.save()

	def __str__(self):
		return self.position

class Education(models.Model):
	start_date = models.DateTimeField(blank=True, null=True)
	start_end = models.DateTimeField(blank=True, null=True)
	qualification = models.CharField(max_length=MAX_LENGTH)
	subject = models.CharField(max_length=MAX_LENGTH)
	institution = models.CharField(max_length=MAX_LENGTH)
	city = models.CharField(max_length=MAX_LENGTH)
	country = models.CharField(max_length=MAX_LENGTH)

	def publish(self):
		self.save()

	def __str__(self):
		return self.subject