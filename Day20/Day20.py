import requests
import sys

if len(sys.argv) < 2 :
    print(f"Usage : {sys.argv[0]} google.com ")

with open("Subdomain.txt") as sub:
    subdomain_list =  sub.read()

subdomain = subdomain_list.splitlines()

for sub in subdomain:
    url = f"http://{sub}.{sys.argv[1]}"
    try:
        requests.get(url)
    except requests.ConnectionError:
        print("......")
        pass
    else:
        print(f"FOUND : {url}")
