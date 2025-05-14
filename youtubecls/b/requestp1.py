
from youtubecls.a.requestp1 import Uday


class Testuday:
    cls=Uday()


    def test_get_details(self):
        resp=self.cls.all_details()
        resp=resp.json()
        print(resp)

    def test_deleted(self):
        resp=self.cls.delete_data()







