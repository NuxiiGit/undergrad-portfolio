from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.utils import timezone

from blog.models import Post
from cv.models import Name, Contact, Skill, Experience, Education

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
	CV_EMAIL = 'example@gmail.com'
	CV_SKILL_TITLE = 'Eating'
	CV_SKILL = 'Lots of food.'

	def setUp(self):
		self.browser = webdriver.Chrome('functional_tests/chromedriver.exe')
		self.URL = self.live_server_url + "/cv"
		Name.objects.create(first=self.CV_NAME, last=self.CV_SURNAME)
		Contact.objects.create(email=self.CV_EMAIL)
		Skill.objects.create(title=self.CV_SKILL_TITLE, description=self.CV_SKILL)
	
	def tearDown(self):
		self.browser.close()

	def test_cv_displays_name(self):
		self.browser.get(self.URL)
		header = self.browser.find_element_by_id("header")
		first_name = header.find_element_by_tag_name("span")
		self.assertEqual(first_name.text, self.CV_NAME + " " + self.CV_SURNAME)
	
	def test_cv_displays_contact(self):
		self.browser.get(self.URL)
		section = self.browser.find_element_by_id("Contact")
		div = header.find_element_by_tag_name("div")
		email = div.find_element_by_class_name("email")
		self.assertEqual(email.text, self.CV_EMAIL)
	
	def test_cv_displays_skill(self):
		self.browser.get(self.URL)
		section = self.browser.find_element_by_id("Skills")
		div = header.find_element_by_tag_name("div")
		title = div.find_element_by_class_name("title")
		desc = div.find_element_by_class_name("desc")
		self.assertEqual(title.text, self.CV_SKILL_TITLE)
		self.assertEqual(desc.text, self.CV_SKILL)

class CvEmptyTestCase(StaticLiveServerTestCase):
	
	def setUp(self):
		self.browser = webdriver.Chrome('functional_tests/chromedriver.exe')
		self.URL = self.live_server_url + "/cv"
	
	def tearDown(self):
		self.browser.close()

	def test_cv_header_default(self):
		self.browser.get(self.URL)
		header = self.browser.find_element_by_id("header")
		default = header.find_element_by_tag_name("span")
		self.assertEqual(default.text, "CV")
	
	def test_cv_contact_default(self):
		self.browser.get(self.URL)
		self.assertRaises(NoSuchElementException, lambda: self.browser.find_element_by_id("Contact"))
	
	def test_cv_skill_default(self):
		self.browser.get(self.URL)
		self.assertRaises(NoSuchElementException, lambda: self.browser.find_element_by_id("Skills"))

	def test_cv_experience_default(self):
		self.browser.get(self.URL)
		self.assertRaises(NoSuchElementException, lambda: self.browser.find_element_by_id("Experience"))
	
	def test_cv_education_default(self):
		self.browser.get(self.URL)
		self.assertRaises(NoSuchElementException, lambda: self.browser.find_element_by_id("Education"))