import pytest


@pytest.mark.borrow
def test_borrow_endpoints(get_request, post_request, put_request, delete_request, config):
    base_endpoint = config["endpoints"]["borrow"]

    # Test: Create a borrow
    add_borrow_data = {"borrowerId": 1, "itemId": 2}
    response = post_request(base_endpoint, add_borrow_data)
    assert response.status_code == 201

    # Test: Get borrow by ID
    borrow_id = response.json().get("id")
    response = get_request(f"{base_endpoint}/{borrow_id}")
    assert response.status_code == 200

    # Test: Update borrow
    update_data = {"itemId": 3}
    response = put_request(f"{base_endpoint}/{borrow_id}", update_data)
    assert response.status_code == 200

    # Test: Delete borrow
    response = delete_request(f"{base_endpoint}/{borrow_id}")
    assert response.status_code == 204
