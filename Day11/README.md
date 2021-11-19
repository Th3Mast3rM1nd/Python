# Day 11

* ***requests Module*** 
```python 
import requests
res = requests.get("https://www.google.com") # get requests
print(res.status_code) # get the status code
print(res.text)
```
```python
import requests 
res = requests.get("https://httpbin.org") 
print(res.headers) # get the respond headers 
print(res.url) # get the url 
```
```python
import requests
headers = {'accept':'application/json'} 
data = {'pass':'Password'} 
url = "https://httpbin.org/post" 
res = requests.post(url,data=data,headers=headers) # sending a post request you can as well send ( head , options , put , delete .... )
if res.status_code == 200:
    print(res.text)
else:
    print(res.status_code)
```
```python
import requests
res = requests.get("https://api.github.com/users/b10ta")
json_data = res.json() # JSON Response Content 
name = ""
followers = ""
for key,value in json_data.items():
    if key == "name":
        name = json_data[key]
        print(f" Name of user is {name}")
    elif key == "followers" :
        followers = json_data[key]
        print(f"{name} has {followers} followers")
```
```python
# cookies 
url = 'https://httpbin.org/cookies'
res = requests.get(url)
res.cookies["admin"] # admin is cookies name for examlpe
cookies = dict(admin='ddddekkewlkd') # to make a dictioanry for the cookies key which is admin and the value is ddddddd ...
r = requests.get(url, cookies=cookies) # send my cookies to the server 

```
```python
# redirection 
import requests
url = "http://github.com" 
res = requests.get(url,allow_redirects=True)
print(res.url) # output will be https://github.com will be redirected because we used http

```


