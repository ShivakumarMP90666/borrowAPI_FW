import pytest


@pytest.mark.wishlist
def test_wishlist_endpoints(get_request, post_request, put_request, delete_request, config):
    base_endpoint = config["endpoints"]["wishlist"]

    # Test: Add new wishlist
    add_wishlist_data = {"userId": 1, "name": "My New Wishlist"}
    response = post_request(base_endpoint, add_wishlist_data)
    assert response.status_code == 200

    # Test: Get wishlist by ID
    wishlist_id = response.json().get("id")
    response = get_request(f"{base_endpoint}/{wishlist_id}")
    assert response.status_code == 200

    # Test: Update wishlist
    update_data = {"name": "Updated Wishlist"}
    response = put_request(f"{base_endpoint}/{wishlist_id}", update_data)
    assert response.status_code == 200

    # Test: Delete wishlist
    response = delete_request(f"{base_endpoint}/{wishlist_id}")
    assert response.status_code == 204
