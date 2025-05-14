import requests

class Main_class:

    url = "https://thinking-tester-contact-list.herokuapp.com/contacts"

    headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NzljZGY1M2EwYTNjZjAwMTMzMWQ1YjkiLCJpYXQiOjE3NDI0Mzg0NDF9.Mh45OXopgivveyIQo8YR4-w_uN4JzO_tikRwfHjEY8M'
    }

    def all_alldata(self):
        resp = requests.get(self.url, headers=self.headers)
        return resp

    def post_data(self, data):
        resp = requests.post(self.url, headers=self.headers, json=data)
        return resp
    #
    # def patch_data(self, data):
    #     id = self.id_generator('nirmal')
    #     self.url = self.url + '/{}'.format(id)
    #     resp = requests.patch(self.url, headers=self.headers, json=data)
    #     return resp
    #
    # def delete_data(self):
    #     id = self.id_generator('nirmal')
    #     url = self.url + '/{}'.format(id)
    #     resp = requests.delete(url, headers=self.headers)
    #     return resp
    #
    # def check_deletedornot(self):
    #     id = self.id_generator('nirmal')
    #     url = self.url + '/{}'.format(id)
    #     resp = requests.get(url, headers=self.headers)
    #     return resp
    #
    # def id_generator(self, name):
    #     resp = self.all_alldata()
    #     resp = resp.json()
    #     for i in resp:
    #         if i["firstName"] == name:
    #             print(i["_id"])
    #             return i["_id"]
    #     return None
