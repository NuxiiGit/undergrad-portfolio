from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.utils import timezone

from .models import Post
from .views import post_list, post_detail

class BlogViewTestCase(TestCase):

	def test_root_url_resolves_to_blog(self):
		found = resolve('/')
		self.assertEqual(found.func, post_list)

	def test_blog_returns_html(self):
		Post.objects.create(title='Sample title', text='Test', published_date=timezone.now())
		request = HttpRequest()
		response = post_list(request)
		html = response.content.decode('utf8').strip()
		self.assertTrue(html.startswith('<html>'))
		self.assertTrue(html.endswith('</html>'))
		print(html)