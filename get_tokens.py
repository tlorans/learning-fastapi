from learning_fastapi.auth_client import AuthClient

# Initialize the AuthClient with the base URL of your FastAPI server
auth_client = AuthClient()

# Obtain the token
token_data = auth_client.get_token("user@example.com", "secret")
if token_data:
    print("Access token obtained successfully")
    print("Access Token:", token_data["access_token"])
else:
    print("Failed to obtain access token")
