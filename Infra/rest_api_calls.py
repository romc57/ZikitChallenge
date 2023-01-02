import requests


def delete_request(url):
    try:
        response = requests.delete(url)
        if response.status_code != 200:
            print('Error ', response.json())
            return False
        return response.text
    except Exception as e:
        print('Error ', e)
        return False


def post_request(url, data):
    try:
        response = requests.post(url, data=data)
        if response.status_code != 200:
            print('Error ', response.json())
            return False
        return response.json()
    except Exception as e:
        print('Error ', e)
        return False


def put_request(url, data):
    try:
        response = requests.put(url, data=data)
        if response.status_code != 200:
            print('Error ', response.json())
            return False
        return response.json()
    except Exception as e:
        print('Error ', e)
        return False

