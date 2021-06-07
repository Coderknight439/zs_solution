from rest_framework.test import APITestCase, APIClient


class TestSetup(APITestCase):
    def setUp(self):
        self.all_country_url = 'http://127.0.0.1:8000/api/get_countries/'
        self.state_url = 'http://127.0.0.1:8000/api/get_state_by_country/'
        self.address_url = 'http://127.0.0.1:8000/api/get_address_by_state/'
        self.address_detail_url = 'http://127.0.0.1:8000/api/get_detail_address/'
        self.client = APIClient()

        return super().setUp()
