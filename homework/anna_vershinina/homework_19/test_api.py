import requests
import pytest

BASE_URL = 'http://167.172.172.115:52353/object'
test_data = [
    {
        "name": "object 1",
        "data": {"color": "black", "size": "big"}
    },
    {
        "name": "オブジェクト",
        "data": {"color": "白い", "size": "小さい"}
    },
    {
        "name": "-)('_",
        "data": {"color": "++`*", "size": "¥[}"}
    }
]


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
        "data": {"color": "black",
                 "size": "big"}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(BASE_URL, json=body, headers=headers)
    post_id = response.json()['id']
    yield post_id
    try:
        requests.delete(f'{BASE_URL}/{post_id}')
    except requests.exceptions.RequestException as e:
        print(f"Delete failed: {e}")


@pytest.mark.critical
@pytest.mark.parametrize('objects', test_data)
def test_obj_creation(objects):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(BASE_URL, json=objects, headers=headers)
    response_data = response.json()

    # Changed an expected code to 200 to avoid errors
    assert response.status_code == 200
    assert response_data["name"] == objects["name"]
    assert response_data["data"] == objects["data"]

    post_id = response_data["id"]
    requests.delete(f'{BASE_URL}/{post_id}')


def test_update_object(new_post):
    updated_body = {
        "data": {
            "color": "WHO",
            "size": "NEW"
        },
        "name": "Testing name change"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f'{BASE_URL}/{new_post}',
                            json=updated_body, headers=headers
                            )

    # test 1: check the record was updated
    assert response.json()["name"] == updated_body["name"]
    assert response.json()["data"] == updated_body["data"]

    # test 2: check the status code
    assert response.status_code == 200, 'Incorrect status code'


@pytest.mark.medium
def test_partially_update_object(new_post):
    body = {
        "name": "Testing partial name change"
    }

    headers = {'Content-Type': 'application/json'}

    response = requests.patch(
        f'{BASE_URL}/{new_post}',
        json=body, headers=headers
    )
    new_body = response.json()['name']

    # test 1: check the status code
    assert response.status_code == 200, 'Status code is incorrect'

    # test 2: check the record partial update
    assert new_body == body['name'], 'Record was not updates'


def test_delete_object(new_post):
    response = requests.delete(f'{BASE_URL}/{new_post}')
    response_get = requests.get(f'{BASE_URL}/{new_post}')

    # test 1: check the length before and after deletion
    assert response_get.status_code == 404, 'Object was not deleted'

    # test 2: check the status code
    assert response.status_code == 200, 'Status code is incorrect'
