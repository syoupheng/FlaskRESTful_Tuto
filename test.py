import requests

data = [{"likes":78, "name":"Joe", "views":80000},
        {"likes":10, "name":"How to make rest API", "views":100000},
        {"likes":35, "name":"Tim", "views":20000}]

BASE = "http://127.0.0.1:5000/"

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()

response = requests.patch(BASE + "video/2", {"name": "Rhoy", "likes": 150})
print(response.json())

input()

response = requests.delete(BASE + "video/2")
print(response)

input()

response = requests.get(BASE + "video/2")
print(response.json())

input()

response = requests.delete(BASE + "video/2")
print(response)
