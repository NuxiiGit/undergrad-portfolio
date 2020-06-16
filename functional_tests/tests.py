from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

import time

class ExampleTestCase(StaticLiveServerTestCase):
	
	def setUp(self):
		self.browser = webdriver.Chrome('functional_tests/chromedriver.exe')
	
	def tearDown(self):
		self.browser.close()

	def test_example(self):
		self.browser.get(self.live_server_url)
		self.assertEquals(1, 1)