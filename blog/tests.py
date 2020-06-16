from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.utils import timezone

from .models import Post
from .views import post_list, post_detail

class BlogViewTestCase(TestCase):

	POST_TITLE = 'Test'
	POST_TEXT = 'Hello world.'

	def setUp(self):
		Post.objects.create(title=self.POST_TITLE, text=self.POST_TEXT, published_date=timezone.now())

	def test_root_url_resolves_to_blog(self):
		found = resolve('/')
		self.assertEqual(found.func, post_list)

	def test_root_equivalent_to_detail_for_singleton_post(self):
		request = HttpRequest()
		response_list = post_list(request)
		response_detail = post_detail(request, 1)
		html_list = response_list.content.decode('utf8')
		html_detail = response_detail.content.decode('utf8')
		self.assertEquals(html_list, html_detail)

	def test_unpublished_post_does_not_affect_post_list(self):
		Post.objects.create(title="Unpublished", text="Work in progress.")
		self.test_root_equivalent_to_detail_for_singleton_post()