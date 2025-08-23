# gallery/tests.py

from django.test import TestCase
from django.urls import reverse

class PageLoadTests(TestCase):
    """
    Tests to ensure that key pages load correctly (return a 200 OK status code).
    """

    def test_home_page_loads(self):
        # 'reverse' gets the URL from the name we gave it in urls.py
        url = reverse('gallery:home')
        response = self.client.get(url)
        # 200 is the HTTP status code for "OK"
        self.assertEqual(response.status_code, 200)

    def test_portfolio_list_page_loads(self):
        url = reverse('gallery:portfolio_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_blog_list_page_loads(self):
        url = reverse('gallery:blog_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

# You can add more complex tests here later, for example:
# - Test that a blog post detail page loads for a published post.
# - Test that a 404 is returned for an unpublished post.
# - Test form submissions.
