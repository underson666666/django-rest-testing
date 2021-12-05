from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from .rest.User import User
# Create your tests here.

class SampleAppTest(TestCase):

    def test_sampleapp1(self):
        factory = APIRequestFactory()
        request = factory.get(reverse('user'))
        view = User.as_view()
        res = view(request)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["hoge"], "hoge")

    def test_sampleapp1_apiclient(self):
        response = APIClient().get(reverse('user'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["hoge"], "hoge")
