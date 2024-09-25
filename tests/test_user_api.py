import requests
import pytest
import json

# Load configuration from config.json
with open('./config/config.json') as config_file:
    config = json.load(config_file)

BASE_URL = config['base_url']
USER_ENDPOINTS = config['user_endpoints']


@pytest.fixture(scope="module")
def user_data_fixture():
    """Fixture to store user data after creation."""
    return {}


def test_create_user(user_data_fixture):
    """Test to create a new user"""
    url = f"{BASE_URL}{USER_ENDPOINTS['create_user']}"
    payload = {
        "id": 140,
        "name": "string",
        "email": "string@example.com",
        "phone": 9878987498,
        "address": [
            {
                "id": 0,
                "addressLine1": "string",
                "addressLine2": "string",
                "city": "string",
                "pincode": 0,
                "type": 0,
                "userId": 0,
                "latitude": 0,
                "longitude": 0,
                "isVerified": True,
                "verifiedDateTime": "2024-09-10T06:24:20.463Z",
                "shopId": 0
            }
        ],
        "profilePicture": "string",
        "notificationToken": "string",
        "isActive": True,
        "uid": "string",
        "role": 0,
        "referralCode": 0
    }
    response = requests.post(url, json=payload)
    user_data = response.json()
    print(response.json())
    print(user_data)
    print(response.status_code)
    assert response.status_code == 200
    user_data_fixture['user_data'] = user_data  # Store created user data in the fixture


def test_get_user(user_data_fixture):
    """Test to get user by ID"""
    user_data = user_data_fixture.get('user_data')
    assert user_data, "User data not found. Please ensure the create_user test is run before this."

    user_id = user_data['id']
    url = f"{BASE_URL}{USER_ENDPOINTS['get_user'].format(Id=user_id)}"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == user_id


def test_update_user(user_data_fixture):
    """Test to update user details"""
    user_data = user_data_fixture.get('user_data')
    assert user_data, "User data not found. Please ensure the create_user test is run before this."

    user_id = user_data['id']
    url = f"{BASE_URL}{USER_ENDPOINTS['update_user']}"
    payload = {
        "id": user_id,
        "name": "John Updated",
        "email": "updatedemail@example.com",
        "phone": 1234567890,
        "address": [
            {
                "id": 0,
                "addressLine1": "updated address",
                "addressLine2": "string",
                "city": "updated city",
                "pincode": 123456,
                "type": 0,
                "userId": user_id,
                "latitude": 0,
                "longitude": 0,
                "isVerified": True,
                "verifiedDateTime": "2024-09-10T06:37:50.863Z",
                "shopId": 0
            }
        ],
        "profilePicture": "updated_picture",
        "notificationToken": "updated_token",
        "isActive": True,
        "uid": "updated_uid",
        "role": 1,
        "referralCode": 12345
    }
    response = requests.put(url, json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == "John Updated"


def test_delete_user(user_data_fixture):
    """Test to delete the user"""
    user_data = user_data_fixture.get('user_data')
    assert user_data, "User data not found. Please ensure the create_user test is run before this."

    user_id = user_data['id']
    url = f"{BASE_URL}{USER_ENDPOINTS['delete_user'].format(Id=user_id)}"
    response = requests.delete(url)
    assert response.status_code == 200
