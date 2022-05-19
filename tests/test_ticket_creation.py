import pytest
from django.urls import reverse
from rest_framework.test import APIClient

client = APIClient


# @pytest.mark.django_db
# def test_user_creation():
#     payload = dict(
#         email="test@example.com",
#         username="testuser",
#         password="testuserpassword"
#     )
#
#     response = client.post(reverse("/^auth/users/"), payload)
#
#     data = response.data
#
#     assert data['issue'] == payload['issue']
#     assert data['description'] == payload['description']
#     assert response.status_code == 201
