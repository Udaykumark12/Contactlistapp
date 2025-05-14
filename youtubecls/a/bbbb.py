import requests

class Main_class:

    url = "https://thinking-tester-contact-list.herokuapp.com/contacts"

    headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NzljZGY1M2EwYTNjZjAwMTMzMWQ1YjkiLCJpYXQiOjE3NDI0Mzg0NDF9.Mh45OXopgivveyIQo8YR4-w_uN4JzO_tikRwfHjEY8M'
    }

    def all_alldata(self):
        resp = requests.get(self.url, headers=self.headers)
        return resp

    def delete___(self):
        url = self.get_user_id("Susmita")
        if url is None:
            print("User ID not found for deletion.")
            return None
        resp = requests.delete(f"{self.url}/{url}", headers=self.headers)
        print("Delete Response:", resp.status_code, resp.text)
        return resp

    def get_user_id(self, firstname):
        resp = self.all_alldata()
        resp = resp.json()
        for i in resp:
            assert  i["firstName"] == firstname, "Firstname not matched"
            print(i["_id"])
            return i["_id"]
        return None



    # def post_data(self,data):
    #     resp = requests.post(self.url, headers=self.headers,json=data)
    #     return resp
    #


    # def get_user_id(self, firstname):
    #     resp = self.all_alldata()
    #     resp = resp.json()
    #
    #     # Assert that at least one match exists
    #     assert any(i["firstName"] == firstname for i in resp), "Firstname '{}' not matched".format(firstname)
    #
    #
    #     # Now that we know a match exists, find and return the _id of the first match
    #     for i in resp:
    #         if i["firstName"] == firstname:
    #             print(i["_id"])
    #             return i["_id"]
    #
    #     return None  # This line shouldn't be reached due to the assert


