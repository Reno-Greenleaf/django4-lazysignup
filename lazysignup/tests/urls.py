from django.urls import path, include
from django.contrib.auth.forms import UserCreationForm

from django.conf import settings

if settings.AUTH_USER_MODEL is 'auth.User':  # pragma: no cover
    from lazysignup.tests.forms import GoodUserCreationForm
else:  # pragma: no cover
    from custom_user_tests.forms import GoodUserCreationForm

from django.contrib import admin

from lazysignup import views
from lazysignup.tests import views as test_views

admin.autodiscover()


# URL test patterns for lazysignup. Use this file to ensure a consistent
# set of URL patterns are used when running unit tests.

from django.contrib import admin

urlpatterns = [
    path(r'^admin/?', admin.site.urls),
    path(r'^convert/', include('lazysignup.urls')),
    path(r'^custom_convert/', views.convert, {
        'template_name': 'lazysignup/done.html'
    }),
    path(r'^custom_convert_ajax/', views.convert, {
        'ajax_template_name': 'lazysignup/done.html'
    }),
]

urlpatterns += [
    path(r'^nolazy/$', test_views.view, name='test_view'),
    path(r'^lazy/$', test_views.lazy_view, name='test_lazy_view'),
]

urlpatterns += [
    path(r'^bad-custom-convert/$', views.convert, {
        'form_class': UserCreationForm}, name='test_bad_convert'),
    path(r'^good-custom-convert/$', views.convert, {
        'form_class': GoodUserCreationForm}, name='test_good_convert'),
]
