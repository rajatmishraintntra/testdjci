from django.test import TestCase

# Create your tests here.

from django.test import TestCase

from website.models import Page


class WebsiteTests(TestCase):
    def test_page_is_created_successfully(self):
        page = Page(
            name='Home',
            slug='home'
        )
        page.save()