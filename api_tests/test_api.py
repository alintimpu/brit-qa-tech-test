import requests
import json

BASE_URL = "https://api.restful-api.dev/objects"
HEADERS = {"Content-Type": "application/json"}

def create_new_object():
    # Creates a new object and returns the ID
    payload = {
        "name": "Initial Object",
        "data": {"attribute1": "value1", "attribute2": "value2"}
    }
    response = requests.post(BASE_URL, json=payload, headers=HEADERS)
    assert response.status_code in [200, 201], f"Expected 200 or 201, got {response.status_code}"
    return response.json().get("id")

def send_patch_request(object_id, payload, expected_status, debug=False):
    # Sends a PATCH request and validates the response status
    response = requests.patch(f"{BASE_URL}/{object_id}", json=payload, headers=HEADERS)
    if debug:
        print(f"PATCH Request: Status Code = {response.status_code}, Response = {response.text}")
    assert response.status_code == expected_status, f"Expected {expected_status}, got {response.status_code}"
    return response.json()

def test_patch_valid_request(object_id):
    payload = {"name": "Updated Name"}
    response_json = send_patch_request(object_id, payload, 200)
    assert response_json.get("id") == object_id, "ID mismatch in response."
    assert response_json.get("name") == "Updated Name", "Name was not updated correctly."

def test_patch_invalid_id():
    send_patch_request("invalid_id", {"name": "Updated Name"}, 404)

def test_patch_empty_payload(object_id):
    send_patch_request(object_id, {}, 404)

def test_patch_invalid_payload(object_id):
    payload = {"invalid_field": "Invalid Value"}
    send_patch_request(object_id, payload, 404)

def test_patch_invalid_data_type(object_id):
    payload = {"name": ["Invalid", "Data", "Type"]}
    send_patch_request(object_id, payload, 400)

def test_patch_special_characters_in_id():
    special_id = "!@#$%^&*()"
    send_patch_request(special_id, {"name": "Updated Name"}, 404)

def test_patch_mixed_valid_invalid_fields(object_id):
    payload = {"name": "Valid Name", "invalid_field": "Invalid Value"}
    response = send_patch_request(object_id, payload, 200)
    assert response.get("name") == "Valid Name", "Valid field was not updated correctly."

def test_patch_large_payload(object_id):
    size = 1000
    while size <= 5000:
        large_payload = {"data": {"nested_field": {"key": "value" * size}}}
        try:
            send_patch_request(object_id, large_payload, 200)
        except AssertionError:
            print(f"Payload of size {size} failed.")
            break
        size += 1000
    print(f"Tested payload sizes up to {size - 1000}.")

if __name__ == "__main__":
    print("Running PATCH endpoint tests...")
    object_id = create_new_object()

    try:
        print("Testing valid PATCH request...")
        test_patch_valid_request(object_id)
        print("Valid PATCH request passed.")

        print("Testing PATCH with invalid ID...")
        test_patch_invalid_id()
        print("PATCH with invalid ID passed.")

        print("Testing PATCH with empty payload...")
        test_patch_empty_payload(object_id)
        print("PATCH with empty payload passed.")

        print("Testing PATCH with invalid payload...")
        test_patch_invalid_payload(object_id)
        print("PATCH with invalid payload passed.")

        print("Testing PATCH with invalid data type...")
        test_patch_invalid_data_type(object_id)
        print("PATCH with invalid data type passed.")

        print("Testing PATCH with mixed valid and invalid fields...")
        test_patch_mixed_valid_invalid_fields(object_id)
        print("PATCH with mixed valid and invalid fields passed.")

        print("Testing PATCH with special characters in ID...")
        test_patch_special_characters_in_id()
        print("PATCH with special characters in ID passed.")

        print("Testing PATCH with large payload...")
        test_patch_large_payload(object_id)
        print("PATCH with large payload test completed.")

    except AssertionError as e:
        print(f"Test failed: {e}")
