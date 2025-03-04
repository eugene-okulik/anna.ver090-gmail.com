import requests


class APITest:

    def __init__(self, base_url):
        self.BASE_URL = base_url

    def get_object_count(self):
        response = requests.get(self.BASE_URL)
        list_length = (len(response.json()['data']))
        return list_length

    def create_object(self):
        old_length = self.get_object_count()
        body = {
            "name": "string",
            "data": {"color": "black",
                     "size": "big"}
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(self.BASE_URL, json=body, headers=headers)

        new_length = self.get_object_count()

        # test 1: check the length update
        assert new_length == old_length + 1, 'New object was not created'

        # test 2: check the status code - found a bug
        try:
            assert response.status_code == 201, 'Status code is incorrect'
        except AssertionError:
            print('Expected status code 201 when new obj is created')

        # return an ID of the created object
        return response.json()['id']

    def update_object(self):
        object_id = self.create_object()
        body = {
            "data": {
                "color": "WHO",
                "size": "NEW"
            },
            "name": "Testing name change"
        }

        (target_name,
         target_data) = (
            body['name'],
            body['data'])

        headers = {'Content-Type': 'application/json'}
        response = requests.put(f'{self.BASE_URL}/{object_id}',
                                json=body, headers=headers
                                )

        # test 1: check the record was updated
        assert (
            response.json()['name'] == target_name
            and response.json()['data'] == target_data
        )

        # test 2: check the status code
        assert response.status_code == 200, 'Incorrect status code'
        self.clear(object_id)

    def partially_update_object(self):
        object_id = self.create_object()

        body = {
            "name": "Testing partial name change"
        }

        headers = {'Content-Type': 'application/json'}

        response = requests.patch(
            f'{self.BASE_URL}/{object_id}',
            json=body, headers=headers
        )

        new_body = response.json()['name']

        # test 1: check the status code
        assert response.status_code == 200, 'Status code is incorrect'

        # test 2: check the record partial update
        assert new_body == body['name'], 'Record was not updates'
        self.clear(object_id)

    def delete_object(self):
        old_length = self.get_object_count()

        object_id = self.create_object()
        response = requests.delete(f'{self.BASE_URL}/{object_id}')
        new_length = self.get_object_count()

        # test 1: check the length before and after deletion
        assert new_length == old_length, 'Deletion was not successful'

        # test 2: check the status code
        assert response.status_code == 200, 'Status code is incorrect'

    def clear(self, post_id):
        requests.delete(
            f'{self.BASE_URL}/{post_id}'
        )


def main():
    api = APITest('http://167.172.172.115:52353/object')

    api.create_object()
    api.delete_object()
    api.update_object()
    api.partially_update_object()


if __name__ == "__main__":
    main()
