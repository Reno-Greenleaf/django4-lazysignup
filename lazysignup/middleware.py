"""Middleware for lazy sign-up."""
from lazysignup.decorators import allow_lazy_user


class AllowLazyUser:
    """Creates/authenticates a lazy user no matter the view."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allow_lazy_user(lambda request: None)(request)
        return self.get_response(request)
