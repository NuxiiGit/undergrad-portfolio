from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.utils import timezone

from blog.models import Post
from cv.models import Name, Contact, Skill, Experience, Education

import time

def show_datetime(dt):
	return dt.strftime("%e %b %Y")

def make_browser():
	op = webdriver.ChromeOptions()
	op.add_argument('headless')
	return webdriver.Chrome(executable_path='functional_tests/chromedriver.exe', options=op)

class BlogTestCase(StaticLiveServerTestCase):
	
	POST_TITLE = 'Test'
	POST_TEXT = 'Hello world.'

	def setUp(self):
		self.browser = make_browser()
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
	CV_PHONE = '+8000'
	CV_SITE = 'example.com'
	CV_SKILL_TITLE = 'Eating'
	CV_SKILL = 'Lots of food.'
	CV_EMPLOYER = 'Outer Space'
	CV_POSITION_TITLE = 'Nothing Inspector'
	CV_POSITION = 'Does absolutely nothing.'
	CV_QUALIFICATION = 'Phd'
	CV_SUBJECT = 'Sleeping'
	CV_INSTITUTION = 'The School'
	CV_CITY = 'Town City'
	CV_COUNTRY = 'Earth'
	CV_TIMEZONE = timezone.now()

	def setUp(self):
		self.browser = make_browser()
		self.URL = self.live_server_url + "/cv"
		Name.objects.create(
				first=self.CV_NAME,
				last=self.CV_SURNAME)
		Contact.objects.create(
				email=self.CV_EMAIL,
				phone=self.CV_PHONE,
				website=self.CV_SITE)
		Skill.objects.create(
				title=self.CV_SKILL_TITLE,
				description=self.CV_SKILL)
		Experience.objects.create(
				employer=self.CV_EMPLOYER,
				position=self.CV_POSITION_TITLE,
				description=self.CV_POSITION,
				start_date=self.CV_TIMEZONE,
				end_date=self.CV_TIMEZONE)
		Education.objects.create(
				qualification=self.CV_QUALIFICATION,
				subject=self.CV_SUBJECT,
				institution=self.CV_INSTITUTION,
				city=self.CV_CITY,
				country=self.CV_COUNTRY,
				start_date=self.CV_TIMEZONE,
				end_date=self.CV_TIMEZONE)
	
	def tearDown(self):
		self.browser.close()
	
	def test_cv_displays_name(self):
		self.browser.get(self.URL)
		header = self.browser.find_element_by_id("header")
		first_name = header.find_element_by_tag_name("span")
		self.assertEqual(first_name.text, self.CV_NAME + " " + self.CV_SURNAME)
	
	def test_cv_displays_contact_email(self):
		self.browser.get(self.URL)
		section = self.browser.find_element_by_id("Contact")
		div = section.find_element_by_tag_name("div")
		email = div.find_element_by_class_name("email")
		self.assertEqual(email.text, self.CV_EMAIL)

	def test_cv_displays_contact_phone(self):
		self.browser.get(self.URL)
		section = self.browser.find_element_by_id("Contact")
		div = section.find_element_by_tag_name("div")
		phone = div.find_element_by_class_name("phone")
		self.assertEqual(phone.text, self.CV_PHONE)

	def test_cv_displays_contact_website(self):
		self.browser.get(self.URL)
		section = self.browser.find_element_by_id("Contact")
		div = section.find_element_by_tag_name("div")
		site = div.find_element_by_class_name("website")
		self.assertEqual(site.text, self.CV_SITE)
	
	def text_cv_contact_website_link_is_correct(self):
		self.browser.get(self.URL)
		section = self.browser.find_element_by_id("Contact")
		div = section.find_element_by_tag_name("div")
		site = div.find_element_by_class_name("website")
		ref = site.get_attribute("href")
		site.click()
		self.assertEqual(self.browser.current_url, ref)
	
	def test_cv_displays_skill_title(self):
		self.browser.get(self.URL)
		section = self.browser.find_element_by_id("Skills")
		div = section.find_element_by_tag_name("div")
		title = div.find_element_by_class_name("title")
		self.assertEqual(title.text, self.CV_SKILL_TITLE)

	def test_cv_displays_skill(self):
		self.browser.get(self.URL)
		section = self.browser.find_element_by_id("Skills")
		div = section.find_element_by_tag_name("div")
		desc = div.find_element_by_class_name("desc")
		self.assertEqual(desc.text, self.CV_SKILL)

	def test_cv_displays_experience_employer(self):
		self.browser.get(self.URL)
		section = self.browser.find_element_by_id("Experience")
		div = section.find_element_by_tag_name("div")
		employer = div.find_element_by_class_name("employer")
		self.assertEqual(employer.text, self.CV_EMPLOYER)
	
	def test_cv_displays_experience_position_title(self):
		self.browser.get(self.URL)
		section = self.browser.find_element_by_id("Experience")
		div = section.find_element_by_tag_name("div")
		position = div.find_element_by_class_name("position")
		self.assertEqual(position.text, self.CV_POSITION_TITLE)
	
	def test_cv_displays_experience_position(self):
		self.browser.get(self.URL)
		section = self.browser.find_element_by_id("Experience")
		div = section.find_element_by_tag_name("div")
		desc = div.find_element_by_class_name("desc")
		self.assertEqual(desc.text, self.CV_POSITION)
	
	def test_cv_displays_experience_start_date(self):
		self.browser.get(self.URL)
		section = self.browser.find_element_by_id("Experience")
		div = section.find_element_by_tag_name("div")
		start_date = div.find_element_by_class_name("start_date")
		self.assertEqual(start_date.text, show_datetime(self.CV_TIMEZONE))
	
	def test_cv_displays_experience_end_date(self):
		self.browser.get(self.URL)
		section = self.browser.find_element_by_id("Experience")
		div = section.find_element_by_tag_name("div")
		end_date = div.find_element_by_class_name("end_date")
		self.assertEqual(end_date.text, show_datetime(self.CV_TIMEZONE))

	def test_cv_displays_education_qualification(self):
		self.browser.get(self.URL)
		section = self.browser.find_element_by_id("Education")
		div = section.find_element_by_tag_name("div")
		qualification = div.find_element_by_class_name("qualification")
		self.assertEqual(qualification.text, self.CV_QUALIFICATION)

	def test_cv_displays_education_subject(self):
		self.browser.get(self.URL)
		section = self.browser.find_element_by_id("Education")
		div = section.find_element_by_tag_name("div")
		subject = div.find_element_by_class_name("subject")
		self.assertEqual(subject.text, self.CV_SUBJECT)

	def test_cv_displays_education_institution(self):
		self.browser.get(self.URL)
		section = self.browser.find_element_by_id("Education")
		div = section.find_element_by_tag_name("div")
		institution = div.find_element_by_class_name("institution")
		self.assertEqual(institution.text, self.CV_INSTITUTION)

	def test_cv_displays_education_city(self):
		self.browser.get(self.URL)
		section = self.browser.find_element_by_id("Education")
		div = section.find_element_by_tag_name("div")
		city = div.find_element_by_class_name("city")
		self.assertEqual(city.text, self.CV_CITY)

	def test_cv_displays_education_country(self):
		self.browser.get(self.URL)
		section = self.browser.find_element_by_id("Education")
		div = section.find_element_by_tag_name("div")
		country = div.find_element_by_class_name("country")
		self.assertEqual(country.text, self.CV_COUNTRY)

	def test_cv_displays_education_start_date(self):
		self.browser.get(self.URL)
		section = self.browser.find_element_by_id("Education")
		div = section.find_element_by_tag_name("div")
		start_date = div.find_element_by_class_name("start_date")
		self.assertEqual(start_date.text, show_datetime(self.CV_TIMEZONE))

	def test_cv_displays_education_end_date(self):
		self.browser.get(self.URL)
		section = self.browser.find_element_by_id("Education")
		div = section.find_element_by_tag_name("div")
		end_date = div.find_element_by_class_name("end_date")
		self.assertEqual(end_date.text, show_datetime(self.CV_TIMEZONE))

class CvPartialTestCase(StaticLiveServerTestCase):
	
	CV_EMAIL = 'helloworld@fakename.com'
	CV_SKILL_TITLE = 'Breathing'
	CV_EMPLOYER = 'Time'
	CV_POSITION_TITLE = 'Ultimate'
	CV_QUALIFICATION = 'Fish'
	CV_SUBJECT = 'Box'
	CV_INSTITUTION = 'Pizza Hut'
	CV_CITY = 'Undefined'
	CV_COUNTRY = 'Object'
	CV_TIMEZONE = timezone.now()

	def setUp(self):
		self.browser = make_browser()
		self.URL = self.live_server_url + "/cv"
		Contact.objects.create(
				email=self.CV_EMAIL)
		Skill.objects.create(
				title=self.CV_SKILL_TITLE)
		Experience.objects.create(
				employer=self.CV_EMPLOYER,
				position=self.CV_POSITION_TITLE,
				start_date=self.CV_TIMEZONE)
		Education.objects.create(
				qualification=self.CV_QUALIFICATION,
				subject=self.CV_SUBJECT,
				institution=self.CV_INSTITUTION,
				city=self.CV_CITY,
				country=self.CV_COUNTRY,
				start_date=self.CV_TIMEZONE)
	
	def tearDown(self):
		self.browser.close()

	def test_cv_contact_no_phone(self):
		self.browser.get(self.URL)
		section = self.browser.find_element_by_id("Contact")
		div = section.find_element_by_tag_name("div")
		self.assertRaises(NoSuchElementException, lambda: div.find_element_by_class_name("phone"))

	def test_cv_contact_no_website(self):
		self.browser.get(self.URL)
		section = self.browser.find_element_by_id("Contact")
		div = section.find_element_by_tag_name("div")
		self.assertRaises(NoSuchElementException, lambda: div.find_element_by_class_name("website"))

	def test_cv_skill_no_description(self):
		self.browser.get(self.URL)
		section = self.browser.find_element_by_id("Skills")
		div = section.find_element_by_tag_name("div")
		self.assertRaises(NoSuchElementException, lambda: div.find_element_by_class_name("desc"))

	def test_cv_experience_no_end_date(self):
		self.browser.get(self.URL)
		section = self.browser.find_element_by_id("Experience")
		div = section.find_element_by_tag_name("div")
		self.assertRaises(NoSuchElementException, lambda: div.find_element_by_class_name("end_date"))

	def test_cv_experience_no_description(self):
		self.browser.get(self.URL)
		section = self.browser.find_element_by_id("Experience")
		div = section.find_element_by_tag_name("div")
		self.assertRaises(NoSuchElementException, lambda: div.find_element_by_class_name("desc"))
	
	def test_cv_education_no_end_date(self):
		self.browser.get(self.URL)
		section = self.browser.find_element_by_id("Education")
		div = section.find_element_by_tag_name("div")
		self.assertRaises(NoSuchElementException, lambda: div.find_element_by_class_name("end_date"))

class CvEmptyTestCase(StaticLiveServerTestCase):
	
	def setUp(self):
		self.browser = make_browser()
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