# Day 7

* ***Functions***

```python 
def greet_user(): # defining a function 
    print("hello")  # block of code 
    
greet_user() # calling the function to be run 
```
```python
def max_number(number): # number is function parameter 
       if number > 100:
          print(f" you choosed the right number ")
       else:
          print("try again")
          
x = 1000
max_number(x) # x is the argument 
```
```python 
# Positional arguments 

def sum_numbers(number1,number2):
    sum = number1 + number2
    print(f" the sum of {number1} and {number2} is {sum}")
    

sum_numbers(10,20)
sum_numbers(100,10000)
```
```python
def host(ip,port):
    print(ip)
    print(port)
    
host(ip="192.178.1.1",port=23) # keyword arguments 
```
```python 
def sum_numbers(x,y=20): # we set the default value of y to 20 
    sum = x + y
    print(sum)
    
sum_numbers(x=20) # output will be 40
sum_numbers(10) # output will be 30
sum_numbers(x=100,y=200) # here we changed the value of y to 200 so the output will be 300
```
```python
def access(username,password):
    access_message = ""
    if username == "root" and password == "toor" :
        access_message = f"Welcome {username}"
        return access_message   # retrun the value of the access_message 
    else:
        access_message = f"{username} or {password} is wrong"
        return access_message 

message = access("root","toor") # the return value is assinged to the variable message 
print(message)
message = access(username="root",password="123")
print(message)
```
```python 
# function and Dictionaries 

def database(name,age,country):
    user = {"username" : name , "user_age" : age , "user_country" : country }
    return user
   
user_1 = database("jon",23,"USA")
user_2 = database("mastermind" , 31 , "Morocco")
print(user_1)
print(user_2)
```
```python 
# functions with while loop
def sum_numbers(number1,number2):
    sum = number1 + number2
    return sum

while True:
    number1 = int(input("Enter your first number"))
    number2 = int(input("Enter your Second number"))
    total = sum_numbers(number1,number2)
    print(total)
    answer = input("to quit enter q ")
    if answer == "q":
        break
    else:
        continue
```
```python
# Functions and Lists 
def sum_of_list(numbers):
    total = 0
    for i in numbers:
        total += i
    return total

list_of_numbers = [10,34,300,22,34,100]
total_sum = sum_of_list(list_of_numbers)
print(total_sum)
```
```python 
# Passing number of arguments to a function 
def sum(*number):
    total = 0
    for i in number:
        total += i
    print(total)

sum(1,3,4,6,77,100)
```
```python
# positional and Arguments
def sum(number,*numbers):
    for i in numbers:
        number += i
    print(number)
    
sum(2,20,20)
```
```python
def user(first,last,**user_data):
       user_data["first_name"] = first
       user_data["last_name"] = last
       return user_data
  
user_info = user("master","mind",location="127.0.0.1",filed="pentesting")
print(user_info)
```

       

