import requests


def test_user_creation(db):
    payload = {"name": "John Doe", "email": "john@example"}
    response = requests.post("https://jsonplaceholder.typicode.com/users", json=payload)

    assert response.status_code == 201

    # Example DB check (pretend you have a users table)
    user = db["fetch_one"](
        "SELECT * FROM users WHERE email=%s", 
        (payload["email"],)
        )
    
    assert user is not None, "User not found in the database"
    assert user["name"] == payload["name"], f"Expected name {payload['name']}, got {user['name']}"

def test_check_users_table(db):
    rows = db["fetch_all"]("SELECT * FROM users")
    print(rows)
    assert isinstance(rows, list)