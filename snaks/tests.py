from django.test import SimpleTestCase
from django.urls import reverse


class TestHome(SimpleTestCase):
    def test_status_code(self):
        url = reverse('home')
        print("\nhome URL:",url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    def test_home_page_templates(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response,  'base.html')


class TestAbout(SimpleTestCase):
    def test_status_code(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    def test_about_page_templates(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'about.html', 'base.html')