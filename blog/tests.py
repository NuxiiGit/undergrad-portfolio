from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from .models import Post
from .views import post_list, post_detail

class BlogViewTestCase(TestCase):

	def test_root_url_resolves_to_blog(self):
		found = resolve('/')
		self.assertEqual(found.func, post_list)

	def test_blog_returns_html(self):
		request = HttpRequest()
		response = post_list(request)
		html = response.content.decode('utf8').strip()
		self.assertTrue(html.startswith('<html>'))
		self.assertTrue(html.endswith('</html>'))
		print(html)