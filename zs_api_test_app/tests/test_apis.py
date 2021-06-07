from .test_setup import TestSetup
from rest_framework import status
from rest_framework.authtoken.models import Token
import requests, json
from ..models import *
from django.conf import settings


class TestAPI(TestSetup):

    def test_all_country_list(self):
        header = {'Authorization': 'Token '+ settings.ACCESS_TOKEN}
        response = requests.get(self.all_country_url, headers=header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.content)
        self.assertEqual(len(data['countries']), 2)
        country_code_bd = requests.get(self.all_country_url+'?code=BD', headers=header)
        data = json.loads(country_code_bd.content)
        self.assertEqual(len(data['countries']), 1)

    def test_country_wise_state_list(self):
        header = {'Authorization': 'Token ' + settings.ACCESS_TOKEN}
        response = requests.get(self.state_url+'1/', headers=header)  # States for Bangladesh
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.content)
        self.assertEqual(len(data['states']), 3)

        state_name_like_dhaka = requests.get(self.state_url+'1/?name=dha', headers=header)
        self.assertEqual(state_name_like_dhaka.status_code, status.HTTP_200_OK)
        data = json.loads(state_name_like_dhaka.content)
        self.assertEqual(len(data['states']), 1)

    def test_state_wise_address_list(self):
        header = {'Authorization': 'Token ' + settings.ACCESS_TOKEN}
        response = requests.get(self.address_url+'11/', headers=header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.content)
        self.assertEqual(len(data['addresses']), 1)

        address_with_house_12 = requests.get(self.address_url+'5/?house_no=12', headers=header)
        self.assertEqual(address_with_house_12.status_code, status.HTTP_200_OK)
        data = json.loads(address_with_house_12.content)
        self.assertEqual(len(data['addresses']), 0)

    def test_address_detail_view(self):
        header = {'Authorization': 'Token ' + settings.ACCESS_TOKEN}
        response = requests.get(self.address_detail_url+'1/', headers=header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = {"name": "Add-1", "road_no": "29", "house_no": "12", "state": "Dhaka", "country": "Bangladesh"}
        data = json.loads(response.content)
        self.assertEqual(res, data['address'])


