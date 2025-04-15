import requests


def names():
    name_list = []
    for i in range(0, 10):
        namex = "uday{}".format(i)
        name_list.append(namex)
    return name_list


url = 'https://httpbin.org/post'


data = {"name":names()}



def login_api():
    response = requests.post(url, json=data)
    print(response.status_code)
    print(response.json())


login_api()
