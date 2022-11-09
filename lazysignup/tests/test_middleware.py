from django.test import TestCase
from lazysignup.models import LazyUser


class MiddlewareTest(TestCase):
	"""Tests for the middleware."""

	def test_created(self):
		"""Lazy user should be available."""
		modification = {'append': 'lazysignup.middleware.AllowLazyUser'}

		with self.modify_settings(MIDDLEWARE=modification):
			response = self.client.get('/lazy-user-available')

		self.assertEqual(response.status_code, 200)

	def test_decorated(self):
		"""The decorator and the middleware together shouldn't create a lazy user twice."""
		modification = {'append': 'lazysignup.middleware.AllowLazyUser'}

		with self.modify_settings(MIDDLEWARE=modification):
			self.client.get('/lazy/')

		self.assertEqual(LazyUser.objects.count(), 1)
