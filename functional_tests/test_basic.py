from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class ExampleTestCase(StaticLiveServerTestCase):
	def test_example(self):
		self.assertEquals(0, 1)