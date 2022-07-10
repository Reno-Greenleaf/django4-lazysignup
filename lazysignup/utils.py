def is_lazy_user(user):
    """ Return True if the passed user is a lazy user. """
    # Anonymous users are not lazy.

    if user.is_anonymous:
        return False

    # Check the user backend. If the lazy signup backend
    # authenticated them, then the user is lazy.
    backend = getattr(user, 'backend', None)
    if backend == 'lazysignup.backends.LazySignupBackend':
        return True

    # Otherwise, we have to fall back to checking the database.
    from lazysignup.models import LazyUser
    return bool(LazyUser.objects.filter(user=user).count() > 0)


def is_ajax(request):
    """Whether a request is AJAX request.

    Should work with jQuery requests.
    """
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'