from youtubecls.a.a import Main_class




class TestLoginContactApp:
    data = {
        "firstName": "k uday",
        "lastName": "kumar",
        "birthdate": "1970-01-01",
        "email": "jdoe@fake.com",
        "phone": "8005555555",
        "street1": "1 Main St.",
        "street2": "Apartment A",
        "city": "Anytown",
        "stateProvince": "KS",
        "postalCode": "12345",
        "country": "USA"
    }

    patch_a={
        "firstName": "Balaji",

    }


    log = Main_class()


    def test_get_request(self):
        resp = self.log.all_alldata()
        assert resp.status_code==200,"no 200"
        resp=resp.json()
        print(resp)

    def test_post_data(self):
        resp = self.log.post_data(self.data)
        assert resp.status_code==201,"no status code"

        resp = self.log.all_alldata()
        resp = resp.json()
        print(resp)


    # def test_patch_data(self):
    #     resp = self.log.patch_data(self.patch_a)
    #     assert resp.status_code==200,"no status code"
    #
    #     resp = self.log.all_alldata()
    #     resp = resp.json()
    #     print("This is response",resp)



    def test_delete_data(self):
        resp = self.log.delete_data()
        assert resp.status_code == 200, "no status code"
        print("deleted succsfuly")








