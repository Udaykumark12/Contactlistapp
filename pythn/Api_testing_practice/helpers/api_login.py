import requests


class Loginhelpers:
    url = "https://thinking-tester-contact-list.herokuapp.com/contacts"

    headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NzljZGY1M2EwYTNjZjAwMTMzMWQ1YjkiLCJpYXQiOjE3NDI0Mzg0NDF9.Mh45OXopgivveyIQo8YR4-w_uN4JzO_tikRwfHjEY8M'
    }

    def get_contact_list_app_users(self):
        response = requests.get(self.url, headers=self.headers)
        return response

    def get_contact_app_details(self, id):
        self.url = self.url + '/{}'.format(id)
        resp = requests.get(self.url, headers=self.headers)
        print(resp.text)
        return resp

    def create_user(self, payload):
        id = self.get_usesr_id("John")
        response = requests.post(self.url, json=payload, headers=self.headers)
        print(response.text)
        return response

    def update_user_details(self, payload):
        id = self.get_user_id("k uday")

        self.url = self.url + '/{}'.format(id)
        response = requests.put(self.url, json=payload, headers=self.headers)
        print(response.text)
        return response

    def update_user_name_with_patch(self, payload):
        id = self.get_user_id("k uday")

        self.url = self.url + '/{}'.format(id)
        response = requests.patch(self.url, json=payload, headers=self.headers)
        print(response.text)
        return response

    def delete_user_details(self):
        id = self.get_user_id('Nirmal')
        print(id)
        self.url = self.url + '/{}'.format(id)
        response = requests.delete(self.url, headers=self.headers)

        res = requests.get(self.url, headers=self.headers)
        print(res)
        return response

    def get_user_id(self, firstname):
        resp = Loginhelpers().get_contact_list_app_users()
        resp = resp.json()
        for data in resp:
            assert data["firstName"] == firstname, "Firstname not matched"
            print(data["_id"])
            return data["_id"]

        return