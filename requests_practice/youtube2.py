import requests


head = {
    'accept': 'text/plain',
    'Content-Type': 'application/json'

}

request_data={
      "id": 160,
      "title": "suday",
      "dueDate": "2025-03-22T03:51:46.232Z",
      "completed": True
    }



url = 'https://fakerestapi.azurewebsites.net/api/v1/Activities'

response = requests.post(url,json=request_data,headers=head)
print(response.status_code)
assert response.status_code==200,"No data found"
resp=response.json()


if isinstance(resp, dict):
    if resp.get("title") == "suday":
        assert resp["id"] == 160, "id does not match, but got {}".format(resp.get("id"))
else:
    # If the response is a list, proceed with your original approach
    for data in resp:
        if data.get("title") == "suday":
            assert data["id"] == 160, "id does not match, but got {}".format(data.get("id"))







# assert resp["id"]==160,"id does not match, but got {}".format(resp.get("id"))



#
# for key, value in resp.items():
#             # print(f"Key: {key}, Value: {value}")
#             # # You can add your assertions here if necessary
#             if key == "id":
#                 assert value == 160, f"id does not match, but got {value}"

