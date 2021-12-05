import requests
import sys
import socket
import json 
if len(sys.argv) == 0:
    print(f"Usage : {sys.argv[0]} url ")


url = str(sys.argv[1])

res = requests.get("https://" + url , verify = False)
if res.status_code == 200:
    print(res.headers)
else:
    print(res.status_code)


gethost = socket.gethostbyname(url)
print(f" the ip addresss of {url} is {gethost} ")

req_location = requests.get(f"https://ipinfo.io/"+ gethost + "/json")
info = json.loads(req_location.text)
for key,value in info.items():
    if key.lower() == "country":
        print(f"The country is : {info[key]}")
    elif key.lower() == "region" :
        print(f"the region is {info[key]} ")
    elif key.lower() == "city" :
        print(f" the city is {info[key]}")


