import requests
import pytest

def test_add_item_to_wishlist(api_config):
    url = f"{api_config['base_url']}/Wishlist/Item"
    data = {
        "wishListId": 92,
        "itemId": 1
    }
    response = requests.post(url, json=data)
    assert response.status_code == 500
    assert response.text == "Item has been added successfully"

def test_get_item_details(api_config):
    url = f"{api_config['base_url']}/Wishlist/Item/92/1"
    response = requests.get(url)
    assert response.status_code == 200
    assert "Item is fetched from the wishlist" in response.text

def test_delete_item_from_wishlist(api_config):
    url = f"{api_config['base_url']}/Wishlist/Item/10"
    response = requests.delete(url)
    assert response.status_code == 200
    assert response.text == "Item has been deleted successfully"

def test_get_user_wishlists(api_config):
    url = f"{api_config['base_url']}/Wishlist/2"
    response = requests.get(url)
    assert response.status_code == 200
    assert "All the details of the wishlists present in an user are retrieved successfully" in response.text

def test_check_item_is_wishlisted(api_config):
    url = f"{api_config['base_url']}/Wishlist/isWishlisted/10/91"
    response = requests.post(url)
    assert response.status_code == 200
    assert response.json() is False

    #changes

