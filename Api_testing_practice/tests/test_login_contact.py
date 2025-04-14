
from Api_testing_practice.helpers.api_login import Loginhelpers


class TestLoginContactApp:

#     my_data={
#     "firstName": "John",
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
#
    # put_data = {
    #     "firstName": "John",
    #     "lastName": "Doe",
    #     "birthdate": "1970-01-01",
    #     "email": "jdoe@fake.com",
    #     "phone": "784332124",
    #     "street1": "1 Main St.",
    #     "street2": "Apartment A",
    #     "city": "Anytown",
    #     "stateProvince": "KS",
    #     "postalCode": "12345",
    #     "country": "USA"
    # }

    patch_data={
        "firstName":"Nirmal"

    }




    def test_verify_contact_list_endpoint(self):
        resp =Loginhelpers().get_contact_list_app_users()
        assert resp.status_code == 200, "Contact list app is not working"
        resp=resp.json()
        print(resp)
        for data in resp:
            assert data.get("firstName") == "Nirmal", "last not name matching"
            assert data.get("lastName") == "kumar", "first not name matching"
            contact_id = data.get("_id")
            print(contact_id)

        # resp=Loginhelpers().get_contact_app_details(contact_id)
        # assert resp.status_code==200
        #

        

    # def test_add_user_to_contact_app_list(self):
    #
    #     resp = Loginhelpers().create_user(self.my_data)
    #     assert resp.status_code==201,"user is not created"
    #     resp=resp.json()
    #     resp=Loginhelpers().get_contact_app_details(resp.get("_id"))
    #     print(resp)


    # def test_update_user_details(self):
    #     resp=Loginhelpers().update_user_details(self.put_data)
    #     assert resp.status_code==200,"user phone not updated"
    #     resp=resp.json()
    #     assert resp["phone"]=="784332124","user details details not updated properly"
    #

    # def test_update_user_details_with_patch(self):
    #     resp=Loginhelpers().update_user_name_with_patch(self.patch_data)
    #     assert resp.status_code==200,"user phone not updated"
    #     resp=resp.json()
    #     assert resp["firstName"]=="Nirmal","user details details not updated properly"

    #
    def test_delete_user(self):
        response = Loginhelpers().delete_user_details()
        if response:
            assert response.status_code == 200, "Failed to delete user"


def test_delete_user(self):
    response = Loginhelpers().delete_user_details()
    if response:
        assert response.status_code == 200, "Failed to delete user"


























