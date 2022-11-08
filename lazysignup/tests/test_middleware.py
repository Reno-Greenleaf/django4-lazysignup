from django.test import TestCase


class MiddlewareTest(TestCase):
	"""Tests for the middleware."""

	def test_created(self):
		"""Lazy user should be available."""
		modification = {'append': 'lazysignup.middleware.AllowLazyUser'}

		with self.modify_settings(MIDDLEWARE=modification):
			response = self.client.get('/lazy-user-available')

		self.assertEqual(response.status_code, 200)
