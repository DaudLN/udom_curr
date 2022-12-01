from http import HTTPStatus
from django.test import TestCase


class TestHomepage(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        assert response.status_code == HTTPStatus.OK
