import requests
import datetime as dt


# The graph is deleted

USERNAME = "notagianttarantula"
TOKEN = "65hgfrye5e6rfgdre5"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

pixela_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor":"yes",
}

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# graph_config = {
#     "id": GRAPH_ID,
#     "name": "Coding graph",
#     "unit": "Min",
#     "type": "int",
#     "color": "momiji",
# }

headers ={
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

my_graph = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/"

response = requests.delete(url=my_graph, headers=headers)
print(response.text)