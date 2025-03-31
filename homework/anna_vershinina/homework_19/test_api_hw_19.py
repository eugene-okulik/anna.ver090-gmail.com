import requests
import pytest
import allure


BASE_URL = 'http://167.172.172.115:52353/object'
test_data = [
    {
        "name": "object 1",
        "data": {"color": "black", "size": "big"}
    },
    {
        "name": "ttt",
        "data": {"color": "rr", "size": "rtg"}
    },
    {
        "name": "-)('_",
        "data": {"color": "++`*", "size": "¥[}"}
    }
]


@allure.feature('Posts')
@allure.story('Create posts')
@pytest.mark.critical
@pytest.mark.parametrize('objects', test_data)
def test_obj_creation(objects):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(BASE_URL, json=objects, headers=headers)
    response_data = response.json()

    with allure.step("Check that status code is 200"):
        assert response.status_code == 200
    with allure.step("Check that object was created"):
        assert response_data["name"] == objects["name"]
        assert response_data["data"] == objects["data"]

    post_id = response_data["id"]
    requests.delete(f'{BASE_URL}/{post_id}')


@allure.feature('Posts')
@allure.story('Update Posts')
@allure.title('WA-99: Test the update of the record (PUT)')
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

    with allure.step("Check the record was updated"):
        assert response.json()["name"] == updated_body["name"]
        assert response.json()["data"] == updated_body["data"]

    with allure.step("Check that status code is 200"):
        assert response.status_code == 200, 'Incorrect status code'


@allure.feature('Posts')
@allure.story('Update Posts')
@pytest.mark.medium
@allure.title('WA-100: Test the partial update of the record (PATCH)')
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

    with allure.step("Check that status code is 200"):
        assert response.status_code == 200, 'Status code is incorrect'

    with allure.step("Check the partial record update"):
        assert new_body == body['name'], 'Record was not updates'


@allure.feature('Posts')
@allure.story('Delete posts')
def test_delete_object(new_post):
    requests.delete(f'{BASE_URL}/{new_post}')
    with allure.step(f'Run GET request for post {new_post}'):
        response_get = requests.get(f'{BASE_URL}/{new_post}')
    with allure.step('Check that status code is 404'):
        assert response_get.status_code == 404, 'Object was not deleted'
    with allure.step('Check that status code is 200'):
        assert response_get.status_code == 200, 'Тест сломан неверным ассертом'


@allure.feature('Example')
@pytest.mark.skip("Irrelevant")
def test_one():
    assert 1 == 2, "Test to see break"


@allure.feature('Example')
def test_two():
    assert 1 == 1
