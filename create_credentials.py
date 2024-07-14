from learning_fastapi.auth_client import AuthClient

# Initialize the AuthClient with the base URL of your FastAPI server
auth_client = AuthClient()

# Read credentials from a file
credentials = auth_client.read_credentials('credentials.txt')

# Register the user (this step can be skipped if the user is already registered)
register_response = auth_client.register_user(credentials["username"], credentials["password"])
if register_response.status_code == 200:
    print("User registered successfully")
else:
    print(f"Failed to register user: {register_response.status_code} - {register_response.text}")
