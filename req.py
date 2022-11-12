import requests
data = {"area": 6.50}
response = requests.post("{}/".format("http://127.0.0.1:5000"), json =data )
print("Price should be "+ str(response.json()))