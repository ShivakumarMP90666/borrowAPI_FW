import pytest


@pytest.mark.delivery
def test_delivery_endpoints(get_request, post_request, config):
    base_endpoint = config["endpoints"]["delivery"]

    # Test: Add a new delivery
    add_delivery_data = {"borrowId": 1, "shopId": 2}
    response = post_request(base_endpoint, add_delivery_data)
    assert response.status_code == 201

    # Test: Get delivery details
    delivery_id = response.json().get("id")
    response = get_request(f"{base_endpoint}/{delivery_id}")
    assert response.status_code == 200
