from selenium import webdriver

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.utils import timezone

from blog.models import Post
from cv.models import Name

import time

class BlogTestCase(StaticLiveServerTestCase):
	
	POST_TITLE = 'Test'
	POST_TEXT = 'Hello world.'

	def setUp(self):
		self.browser = webdriver.Chrome('functional_tests/chromedriver.exe')
		self.URL = self.live_server_url
		Post.objects.create(title=self.POST_TITLE, text=self.POST_TEXT, published_date=timezone.now())
	
	def tearDown(self):
		self.browser.close()

	def test_homepage_correctly_displays_blog_post(self):
		self.browser.get(self.URL)
		post = self.browser.find_element_by_id(self.POST_TITLE)
		body = post.find_element_by_class_name('body')
		self.assertEqual(body.text, self.POST_TEXT)
	
	def test_homepage_correctly_redirects_to_cv(self):
		self.browser.get(self.URL)
		self.browser.find_element_by_id("cv").click()
		self.assertEqual(self.browser.current_url, self.URL + "/cv")

class CvTestCase(StaticLiveServerTestCase):
	
	CV_NAME = 'Mann'
	CV_SURNAME = 'Darin'

	def setUp(self):
		self.browser = webdriver.Chrome('functional_tests/chromedriver.exe')
		self.URL = self.live_server_url + "/cv"
		Name.objects.create(first=self.CV_NAME, last=self.CV_SURNAME)
	
	def tearDown(self):
		self.browser.close()

	def test_cv_displays_name(self):
		self.browser.get(self.URL)
		header = self.browser.find_element_by_id("header")
		first_name = header.find_element_by_tag_name("span")
		self.assertEqual(first_name.text, self.CV_NAME + " " + self.CV_SURNAME)