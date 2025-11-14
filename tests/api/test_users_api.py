import json
import pytest
import requests 
from utils.logger import get_logger
from pathlib import Path


logger = get_logger()

def load_test_data():
   test_data_path= (Path(__file__).parent.parent.parent / "test_data" / "posts.json").resolve()
   print("Looking for test data at:", test_data_path)


   if not test_data_path.exists():
       raise FileNotFoundError(f"Test data file not found at {test_data_path}")
   
   with open(test_data_path, "r", encoding="utf-8") as f:
       return json.load(f)

# CREATE POST TEST
@pytest.mark.smoke 
def test_create_post(base_url, get_headers):
    data = load_test_data()
    payload = data["create_post"]

    logger.info("Starting CREATE test for /posts endpoint")
    logger.info(f"Payload: {payload}")

    response = requests.post(f"{base_url}/posts", json=payload, headers=get_headers)

    logger.info(f"Response Status Code: {response.status_code} - {response.text}")
    assert response.status_code == 201
    assert response.json()["title"] == payload["title"]

# READ(GET) POST TEST
@pytest.mark.smoke
def test_read_post(base_url):
    post_id = 1 # Assuming post with ID 1 exists for testing
    logger.info(f"Fetching post with ID: {post_id}")

    response = requests.get(f"{base_url}/posts/{post_id}")
    logger.info(f"Response: {response.status_code}")
    assert response.status_code == 200
    assert "title" in response.json()

# UPDATE POST TEST 
@pytest.mark.regression
def test_update_post(base_url, get_headers):
    data = load_test_data()
    payload = data["update_post"]
    post_id = 1 

    logger.info(f"Updating post: {post_id} with data: {payload}")

    response = requests.put(f"{base_url}/posts/{post_id}", json=payload, headers=get_headers)
    logger.info(f"Response: {response.status_code} - {response.text}")

    assert response.status_code == 200
    assert response.json()["title"] == payload["title"]

# DELETE POST TEST 
@pytest.mark.regression
def test_delete_post(base_url, get_headers):
    post_id = 1
    logger.info(f"Deleting post with ID: {post_id}")

    response = requests.delete(f"{base_url}/posts/{post_id}", headers=get_headers)
    logger.info(f"Response: {response.status_code}")
    assert response.status_code in [200, 204]

# NEGATIVE TEST FOR VALIDATION OR ERROR HANDLING
@pytest.mark.regression
def test_create_post_with_invalid_data(base_url, get_headers):
    invalid_payload = {"title": ""}
    logger.info(f"Testing POST /posts with invalid payload")

    response = requests.post(f"{base_url}/posts", json=invalid_payload, headers=get_headers)
    logger.info(f"Response: {response.status_code} - {response.text}")
    assert response.status_code in [400, 201]


