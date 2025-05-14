
from youtubecls.a.bbbb import Main_class


class TestLoginContactApp:
    log = Main_class()

    # my_data = {
    #     "firstName": "Susmita",
    #     "lastName": "Doe",
    #     "birthdate": "1970-01-01",
    #     "email": "jdoe@fake.com",
    #     "phone": "8005555555",
    #     "street1": "1 Main St.",
    #     "street2": "Apartment A",
    #     "city": "Anytown",
    #     "stateProvince": "KS",
    #     "postalCode": "12345",
    #     "country": "USA"
    # }






    def test_get_request(self):
        resp = self.log.all_alldata()
        assert resp.status_code==200,"no 200"
        resp=resp.json()
        print(type(resp))
        print(resp)


    def test_data__(self):
        resp=self.log.delete___()
        print("this is delete",resp)



    # def test_post_data_(self):
    #     resp=self.log.post_data(self.my_data)
    #     assert resp.status_code == 201, "no status code"
    #
    #     resp = self.log.all_alldata()
    #     resp = resp.json()
    #     print("this resp", resp)


