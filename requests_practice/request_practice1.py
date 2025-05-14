import requests
url = 'https://httpbin.org/post'
data = {
    'name': 'John Doe',
    'age': 30
}

response = requests.post(url,data=data)

# Print the response
print(response.status_code)  # Status code
print(response.text)          # Response body
