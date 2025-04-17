import requests


class APIS:
    url = 'https://fakerestapi.azurewebsites.net/api/v1/Activities'

    def c(self):
        self.header = {
            'accept': 'application/json',  # Corrected content type
            'Content-Type': 'application/json'
        }

    def gett(self,end):
        self.c()
        url=self.url+"{}".format(end)
        response = requests.get(self.url, headers=self.header)
        return response


    def get_id(self):
        self.c()
        response = requests.get(self.url, headers=self.header)
        resp=response.json()
        for i in resp:
            assert i["id"]==1,"id miss match"
            print(i["id"])
            return i["id"]

        return


    def delete_id(self):
        self.c()
        url = self.url + "{}".format(self.get_id())
        response = requests.delete(self.url, headers=self.header)
        return response










