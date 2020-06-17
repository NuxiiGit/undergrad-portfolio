from django.conf import settings
from django.db import models
from django.core import validators

MAX_LENGTH = 255

class Name(models.Model):
	first = models.CharField(max_length=16, default="")
	last = models.CharField(max_length=16, default="")

	def publish(self):
		self.save()

	def __str__(self):
		return self.first + " " + self.last

class Contact(models.Model):
	email = models.EmailField(max_length=MAX_LENGTH, null=True)
	phone = models.CharField(max_length=16, default="+000", validators=[validators.RegexValidator(r'\+(\d+)')])
	website = models.URLField(default='')

	def publish(self):
		self.save()

	def __str__(self):
		return self.email

class Skill(models.Model):
	title = models.CharField(max_length=MAX_LENGTH, null=True)
	description = models.TextField()

	def publish(self):
		self.save()

	def __str__(self):
		return self.title

class Experience(models.Model):
	start_date = models.DateTimeField(null=True)
	end_date = models.DateTimeField(null=True)
	employer = models.CharField(max_length=MAX_LENGTH, null=True)
	position = models.CharField(max_length=MAX_LENGTH, null=True)
	description = models.TextField()

	def publish(self):
		self.save()

	def __str__(self):
		return self.position

class Education(models.Model):
	start_date = models.DateTimeField(null=True)
	end_date = models.DateTimeField(null=True)
	qualification = models.CharField(max_length=MAX_LENGTH, null=True)
	subject = models.CharField(max_length=MAX_LENGTH, null=True)
	institution = models.CharField(max_length=MAX_LENGTH, null=True)
	city = models.CharField(max_length=MAX_LENGTH, null=True)
	country = models.CharField(max_length=MAX_LENGTH, null=True)

	def publish(self):
		self.save()

	def __str__(self):
		return self.subject