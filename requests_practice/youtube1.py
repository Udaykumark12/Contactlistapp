import requests
head = {
    'accept': 'text/plain',
    'Content-Type': 'application/json'

}
data={"id":3,"title":"uday","dueDate":"2025-03-22T14:13:30.086793+00:00","completed":True}

url = 'https://fakerestapi.azurewebsites.net/api/v1/Activities'


response = requests.get(url)

print(response.text)
print(response.status_code)
resp=response.json()


for i in resp:
    if i.get("id")==3:
        c=i.get("id")

resp = requests.put(url+'/{}'.format(c),headers=head,json=data)
print(resp.text)
print(resp.status_code)

 
print(c)