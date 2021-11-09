# Day 5

* ***Dictionaries*** 

```python 
person = {"name" : "mastermind" , "email" : "b10ta@protonmail.com" , "location" : 127.0.0.1 } # key:value 
print(person["name"]) # value of the key (name )
print(person["location"])
admin_email = person["email"]
print(f" The email Admin is {admin_email}")
person["password"] = "PassWord@2020" # adding new key-value to the Dictionary 
person["age"] = 30  # adding new key-value to the Dictionary
person["password"] = "Password2022" # modifying value of Password
```
```python 
car = { "color" : "green" , "speed" : "meduim" , "engine" : "benzin" }
del car["engine"] # Removing key-value Pairs
print(car) 
```
```python 
favorite_language = { 
                      "david" : "java",
                      "youssef" : "python",
                      "sarah" : "C#",
                      "mery" : "Js",
}
nobody = favorite_language.get("nobody" : "C++" ) # get() will get the key of nobody if exist , if doesnt exist will get the default value C++
print(nobody)
```
* ***looping Through a Dictionary***

```python 
users = {
        "user1" : "admin",
        "user2" : "guest",
        "user3" : "mastermind",
}
for user_id, username in users.itmes(): #items() method return a list of key-value pairs .
    print(f"User_ID : {user_id}")
    print(f"Username" : {username}")

# looping Through just the keys
for userid_keys in users.keys() # keys() method return a lif of keys 
    print(f"Username" : {userid_keys.title()}")
```
```python 
database = {"admin" : "user1" , "mastermind" : "user2" , "guest" :"user3" ,}
admins = ["admin" , "mastermind" ]
for user in database.keys():
    if user in admins :
        print(f" welcome {user} you have access to the panel")
    else:
        print(f" Welcome {user} you dont have access to the panel")
```
```python 
names = {"admin" : 1 , "guest" : 4 , "mastermind" : 10 , "nobody" : 10 }
for name in sorted(names.keys()):  # sorted() function is used to sort the keys in a dictionary 
    print(f"{name}")
 
for number in names.values(): # looping through the values using values()  method 
    print(number)

for uniq_number in set(names.values()): # set() to get just uniq values 
    print(uniq_number)
```
* ***Nesting***

```python 
# a list of Dictionaries
database1 = {"user1" : "admin" , "user2" :"mastermind" , "user3" : "guest" }
database2 = {"user1" : "nobody" , "user2" : "joker" , "user3" : "guest1" }
database3 = {"user1" : "root" , "user2" : "jen" , "user3" : "somebody" }
databases = [ database1 , database2 , database3 ]
for database in databases :
    print(database)

print(f" The total number of databases is {len(databases)}")
```
```python
# a List in a Dictionary 
users = {
       "user" : "admin",
       "info" : [ "31 years old " , "youssef" , "175 cm " ],
}
print(f" the user {users['user']} "
for info in users["info"]:
    print(f"\t{info}")
```
```python 
# A Dictionary in a Dictionary 
users = {
       "admin" : {
            "first_name" : "master" , 
            "last_name"  : "mind" ,
            "location"   : "127.0.0.1" ,
            },
       "user_1" : {
             "first_name" : "you" , 
             "last_name" : "somone" ,
             "location"  : "France" ,
             },
}

for username , user_info in users.items():
    print(f"Username : {username} ")
    full_name = f"{user_info['first_name']} {user_info['last_name']}"
    location = user_info['location']
      
    print(f"\t Full name : {full_name.title()}")
    print(f"\t Location : {location.title()}")
```

               
           
 


