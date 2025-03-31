import pytest
import requests

BASE_URL = 'http://167.172.172.115:52353/object'


@pytest.fixture(scope='session', autouse=True)
def print_start_finish():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture(scope='function', autouse=True)
def print_before_after_test():
    print('before test')
    yield
    print('after test')


@pytest.fixture()
def new_post():
    body = {
        "name": "string",
        "data": {"color": "black", "size": "big"}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(BASE_URL, json=body, headers=headers)
    post_id = response.json()['id']
    yield post_id
    try:
        requests.delete(f'{BASE_URL}/{post_id}')
    except requests.exceptions.RequestException as e:
        print(f"Delete failed: {e}")
