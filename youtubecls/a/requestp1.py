

import requests




class Uday:

    url = "https://thinking-tester-contact-list.herokuapp.com/contacts"

    headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NzljZGY1M2EwYTNjZjAwMTMzMWQ1YjkiLCJpYXQiOjE3NDI0Mzg0NDF9.Mh45OXopgivveyIQo8YR4-w_uN4JzO_tikRwfHjEY8M'
    }

    def all_details(self):
        resp=requests.get(self.url,headers=self.headers)
        return resp

    def capture_id(self,name):
        resp=self.all_details()
        resp=resp.json()
        for i in resp:
            try:
                assert i.get("firstName")==name
                print(i["_id"])
                return i["_id"]
            except:
                print("no name is found")

        return None

    def delete_data(self):
        resp=self.capture_id("k uday")
        url=self.url+"/{}".format(resp)

        resp=requests.delete(url,headers=self.headers)
        print(resp.status_code, resp.text)

