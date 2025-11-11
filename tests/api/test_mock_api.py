import requests
import requests_mock

def test_mocked_get_request():
    url = "https://fakeapi.com/users/1"
    with requests_mock.Mocker() as mock:
        mock.get(url, json={"id": 1, "title": "Mock Post"}, status_code=200)

        response = requests.get(url)
        assert response.status_code == 200
        assert response.json()["title"] == "Mock Post"

# This is super useful for isolating tests during local dev or when a real API is unavailable.