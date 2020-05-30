import requests

def client():

    # credentials = {"email": "andreas.siedler@gmail.com", "password": "gippo000"}
    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/", data=credentials)

    token_h = "Token 540ac7cae3cc9d2647ec681fda1c5c35b2f36513"
    headers = {"Authorization": token_h}
    response = requests.get("http://127.0.0.1:8000/api/v1/profiles/candidates/", headers=headers)

    print("Status Code: ", response.status_code)    
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()