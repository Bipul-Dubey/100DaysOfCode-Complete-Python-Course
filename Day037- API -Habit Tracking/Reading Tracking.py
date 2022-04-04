import requests
from datetime import datetime
USERNAME="johnn"
TOKEN="asdfghjkl"
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

view_user="https://pixe.la/@johnn"

Graph_id="graph2"
graph_params={
    "id":Graph_id,
    "name":"Cycling Graph",
    "unit":"pages",
    "type":"float",
    "color":"ajisai"
}
headers={
    "X-USER-TOKEN":TOKEN
}

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
# response=requests.post(url=graph_endpoint,json=graph_params,headers=headers)

today=datetime.now()
formatdate=today.strftime("%Y%m%d")

do=input("post\nupdate\ndelete\nWhat you want to do?? ").lower()
if do=='post':
    pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{Graph_id}"
    pixela_data = {
        "date": formatdate,
        "quantity": input("How Many Pages You Read Today?? "),
    }
    response = requests.post(url=pixel_creation_endpoint, json=pixela_data, headers=headers)
elif do=='update':
    update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{Graph_id}/{formatdate}"
    new_pixel_data = {
        "quantity": input("Update: ")
    }
    response=requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)
elif do=='delete':
    delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{Graph_id}/{formatdate}"
    response=requests.delete(url=delete_endpoint,headers=headers)


# link to view page
"https://pixe.la/v1/users/johnn/graphs/graph2.html"