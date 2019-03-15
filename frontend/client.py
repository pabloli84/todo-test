import requests

api_address = 'http://localhost:5001'


def add_user(user_name):
    user_url = "{url}/users".format(url=api_address)
    r = requests.put(user_url, data={'user_name': user_name})

    return r.status_code, r.text
