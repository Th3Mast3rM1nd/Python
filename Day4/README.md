# Day 4 

* ***Slicing a List***
```python 
country = ["Germany","France","Holand","Norway"]
print(country[0:3])

first_country = country[0:1]  
print(first_country)

last_country = country[-1]
print(last_country)

players = ["Player1","Player2","Player3","Player4"]
for player in players[:3]
    print(player.title())
```
* ***Tuples***
```python 
numbers=("100","220","33")
numbers[0]
numbers[1]
numbers[2]

for number in numbers:
    print(number)   
```
* ***IF Statements***

```python
countries=["France","Gemrany","Holand","USA"]
for country in dountries:
    if country == "France" :
        print(f"{country.upper()} i Have Visited")
    else:
        print(f"{country.title()} Looking for to visit it ")
# Checking For Equality 
number = 1
name = "mastermind"
if number == 1 :
   print("True")
if number < 1 : # >= , > , <=  , != 
   print(f"number is less than {number}")
if name == "mastermind":
   print(name)
if name != "mastermind": # dosent equal sign 
   print(f"{name} dosent equal mastermind")

# if Conditions 
age = 30
if age < 40 and age >= 30 :
   True
if age >= 40 or age <= 30 :
   True

# if and Lists 
numbers = [1,4,5,7,10,30,20]
number = 10
if number in numbers:
   print(f"{number} was found in the list")
if number not in numbers:
   print(f"{number} was not found in the list")
# Boolean Experssions
True
False
if number in numbers:
   True
else:
   False
```
```python
age = 12 
if age < 4 :
   price = 0
elif age < 18:
   price = 25
elif age < 65:
   price = 40
elif >= 65:
   price = 20
print(f"Your admission cost is ${price}")

   



