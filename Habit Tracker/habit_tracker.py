import requests
from datetime import datetime as dt

USERNAME = "vighnesh"
TOKEN = "adhsnasjfnkj"
graph="graph2"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
print("User creation:", response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph2",
    "name": "Studying graph",
    "unit": "Hour",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print("Graph creation:", response.text)

pixel_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{graph}"

today=dt(year=2025,month=10,day=4)

graph_pixel={
    "date":today.strftime("%Y%m%d"),
    "quantity":"8",
}

response = requests.post(url=pixel_endpoint, json=graph_pixel, headers=headers)
print("Graph pixel:", response.text)

pixelupdate_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph}/{today.strftime('%Y%m%d')}"


pixelupdate={
    "quantity":"4"
}

response = requests.put(url=pixelupdate_endpoint, json=graph_pixel, headers=headers)
print(" pixel update:", response.text)

