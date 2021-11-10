# Day 6

* ***User Input***
```python
# input() function used to ask user for an input 

name = input("Enter your name Here : ")
print(f"\tHello , {name.title()}")

# int() to accept integer inputs
age = int(input("Enter your age  : ")) 
print(f"You are {age} years Old")
# Even or Odd number checker 
number = input("Enter a Number to Check if its even or odd  " )
number = int(number)
if number % 2 == 0 :
   print(f"\n The number {number} is Even ")
else:
   print(f"\nThe number {number} is odd " )
```
* ***While Loops***
```python
number = 0
while number != 10:
      number = int(input("Enter a number "))
      print(f" The number you enterd is {number}")
      if number == 10 :
         print(f"Great right number ")
      else:
          print(f"Try again")
```

```python 
number = 1
while number <= 5:
    print(number)
    number += 1

```
```python
# using what called a flag 

active = True 
while active :
    number = input(" Enter your number " )
    number = int(number)
    if number == 10 :
       active = Flase
    else:
       print("Try again")

```
```python 
# break to exit a loop or Contuine 
ip_list = ["192.168.1.1", "192.168.1.110" , "192.168.1.122" , "10.10.1.1"]
while True:
    host = input("Enter ip Here ")
    if host in ip_list :
       print(f"{host} already in the list")
       break 
    else:
       ip_list.append(host)
       print(f" The {host} was added to the list : {ip_list}")
       continue
```
* ***While loop with lists and Dictionaries***

```python 
# moving itmes from a list to another 

new_users = ["root" , "admin" , "guest" ]
users = []
while new_users :
    user = new_users.pop()
    users.append(user)
    
for username in users:
    print(f" This user {username} was added to the database ")

# removing a specific value from a list 

while "guest" in users :
    users.remove("guest")
print(users)

```
```python 
database = {}
active = True
while active :
    username = input(" Enter your username ")
    password = input(" Enter your  password ")
    database[username] = password

    answer = input(" Would like to add new user yes or no ")
    if answer == "no":
        active = False

print(f" Here is the names of the users we have so far ")
for user,passwd in database.items():
    print(f"{user.title()}")

```


    
