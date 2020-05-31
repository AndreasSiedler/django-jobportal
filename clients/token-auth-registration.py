import requests

def client():

    data = {
    "email": "test@test.com",
    "password1": "ujmik,ol.",
    "password2": "ujmik,ol."
    }

    # token_h = "Token 640c2db3fafd2ad1f2e5c5e4ececb256c7fcdcef"
    # headers = {"Authorization": token_h}
    # response = requests.get("http://127.0.0.1:8000/api/profiles/", headers=headers)
    try:
        response = requests.post("http://127.0.0.1:8000/rest-auth/registration/", data=data)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        raise SystemExit(e)

    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()