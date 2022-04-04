import requests
from datetime import datetime
USERNAME="bipul"        # give username what you want
TOKEN="qwertyuiop"      # create token what you want but letter must be 8-128
pixela_endpoint="https://pixe.la/v1/users"

user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# create user account
# this below line work if user not created
# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

# create a graph definition
Graph_id="graph1"
graph_params={
    "id":Graph_id,
    "name":"Cycling Graph",
    "unit":"KM",
    "type":"float",
    "color":"ajisai"
}
headers={
    "X-USER-TOKEN":TOKEN
}

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"

# this work only once to create graph
# response=requests.post(url=graph_endpoint,json=graph_params,headers=headers)
# print(response.text)

# updating pixela
pixel_creation_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{Graph_id}"

today=datetime.now()
formatdate=today.strftime("%Y%m%d")

pixela_data={
    "date":formatdate,
    "quantity":input("How Many kilometer did you Cycle?? "),
}

response=requests.post(url=pixel_creation_endpoint,json=pixela_data,headers=headers)
print(response.text)

update_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{Graph_id}/{formatdate}"
new_pixel_data={
    "quantity":"500"
}

# response=requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)
# print(response.text)

delete_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{Graph_id}/{formatdate}"
# response=requests.delete(url=delete_endpoint,headers=headers)
# print(response.text)