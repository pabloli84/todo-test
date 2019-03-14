import requests

api_address = 'http://localhost:5001'


def add_user(user_name):
    user_url = api_address.join('/users')
    r = requests.put(user_url, data={'user_name' : user_name})

    return r
