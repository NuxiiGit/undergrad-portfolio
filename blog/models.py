from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core import validators

class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

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