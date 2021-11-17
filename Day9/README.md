# Day 9

* ***Exceptions ( Error Handling )***
```python 
# ZeroDivisionError 

x = int(input("Enter your first number "))
y = int(input("Enter your second number "))

if y == 0 and x > 0:
    try:
        print(x / y)
    except ZeroDivisionError:
        print(f" you cant Divide by zero")
else:
    print(x / y)
```
```python
# FileNotFoundError 
# try-except-else
filename = "file.txt"

try:
    with open(filename) as file_contents:
        contents = file_contents.read()
except FileNotFoundError:
    print("File Not found")

else:
    print(len(contents))
```
```python 
# pass > to pass the error and not print the output

try:
    print(10/0)
except ZeroDivisionError:
    pass
```
* ***Stroing Data ( Json Module )***
```python 
# json.dump to store the data in a file
import json
names = ["mastermind" ,"root" , "admin"]

with open("names.json","w") as file:
    json.dump(names,file)

```
```python 
# json.load to read data from a json file
filename = "names.json"
with open(filename) as file_json:
    names = json.load(file_json)
    
print(names)
```
```python 
import json 
filename = "username.json"
try:
   with open(filename) as f:
   username = json.load(f)
except FileNotFoundError:
   username = input("Enter your name Here ")
   with open(filename, "w" ) as f:
   json.dump(username , f)
   print(f" {username} added to the file")
else:
  print(f"Welcome Back {username}")

```

