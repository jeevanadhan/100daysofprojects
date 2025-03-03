import requests
import datetime
pixela_endpoint="https://pixe.la/v1/users"
TOKEN="kdjfoajenfnaksjnff hello"
USERNAME="jeeva1"
my_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
# response=requests.post(url=pixela_endpoint,json=my_params)
# print(response.text)
GRAPHID="graph1"
graph_config={
    "id":GRAPHID,
    "name":"GRAPH",
    "unit":"km",
    "type":"float",
    "color":"kuro"
}
header={
    "X-USER-TOKEN":TOKEN
}
# graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_response=requests.post(url=graph_endpoint,json=graph_config,headers=header)
# print(graph_response.text)

pixela_creation_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
today = datetime.datetime.now()


pixela_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? "),
}
# POSTING

response = requests.post(url=pixela_creation_endpoint, json=pixela_data, headers=header)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}
## PUT
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)


delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"


## DELETE
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)