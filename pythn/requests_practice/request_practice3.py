import requests

url = "https://www.redbus.in/search/SearchV4Results?fromCity=122&toCity=123&src=Bangalore&dst=Chennai&DOJ=11-Feb-2025&sectionId=0&groupId=0&limit=0&offset=0&sort=0&sortOrder=0&meta=true&returnSearch=0"

# If you're sending form data, use `data`
payload = {
    "src": "bangalore",
    "dst": "chennai"
}

# Headers (optional)
headers = {
    "User-Agent": "Mozilla/5.0"  # A common header to mimic a browser request (if necessary)
}

# Send the POST request
response = requests.post(url, headers=headers, data=payload)

# Print the response text (HTML or JSON depending on the response)
print(response.text)
