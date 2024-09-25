import pytest
import requests
import json

# Read the config file and share it across tests
@pytest.fixture(scope="session")
def config():
    with open("./config/config.json") as config_file:
        return json.load(config_file)

# Base URL fixture for making API requests
@pytest.fixture(scope="session")
def base_url(config):
    return config["base_url"]

# Fixture for setting up the headers
@pytest.fixture
def headers():
    return {"Content-Type": "application/json"}

# Fixture to send GET request
@pytest.fixture
def get_request(base_url):
    def _get(endpoint, params=None):
        response = requests.get(f"{base_url}{endpoint}", params=params)
        return response
    return _get

# Fixture to send POST request
@pytest.fixture
def post_request(base_url):
    def _post(endpoint, data):
        response = requests.post(f"{base_url}{endpoint}", json=data)
        return response
    return _post

# Fixture to send PUT request
@pytest.fixture
def put_request(base_url):
    def _put(endpoint, data):
        response = requests.put(f"{base_url}{endpoint}", json=data)
        return response
    return _put

# Fixture to send DELETE request
@pytest.fixture
def delete_request(base_url):
    def _delete(endpoint):
        response = requests.delete(f"{base_url}{endpoint}")
        return response
    return _delete
