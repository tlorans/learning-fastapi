import requests

class AuthClient:
    BASE_URL = "http://127.0.0.1:8000"

    @staticmethod
    def get_token(username, password):
        token_url = f"{AuthClient.BASE_URL}/auth/token"
        token_payload = {
            "username": username,
            "password": password
        }
        token_headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response = requests.post(token_url, data=token_payload, headers=token_headers)
        print(f"URL: {token_url}")
        print(f"Payload: {token_payload}")
        print(f"Response status code: {response.status_code}")
        print(f"Response text: {response.text}")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to obtain access token: {response.status_code} - {response.text}")
            return None