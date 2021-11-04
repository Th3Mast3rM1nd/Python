# Python Part 1

```python 
print("Welcome to Part One")
```
* ***variables***
```python 
name = "mastermind" # variable names can contain letters , numbers , underscroes but no spaces
print(name)
# strings 
name_1= "python basics"
print(name_1.title()) # title() is method to change eacj word to title case
print(name_1.upper())
print(name_1.lower()) 

job_title = "manager"
job_title_1 = "sell"
company = " google"
job = f"{job_title_1} {job_title}" # format strings used here to replace the name of any variable in braces {} with its value.
print(job.title())
print(f" im working as {job.title()} in this {company.title()})"

string_with_space = "   mastermind"
string_with_space_1 = "Pentesting    "
print(f"{string_with_space.lstrip()}") # strip the space from the left
print(f"{string_with_space_1.rstrip()}") # strip the space from the right
print(f"{string_with_space.strip()}") # strip the space from the string ( left and right )

number = 10_100_0000_0000_0000 # underscore used to group long numbers to be more readable 
print(number)
number1 , number2 , number3 = 10 , 20 , 30 # Multiple assignment
```
* ***Lists*** 

```python
country=['Germany','England','Italy','   france'] # 
print(country) # will print all the item on the list
print(country[0]) # print the county on index 0 ( lists start with 0 not 1 ) Germany
print(county[1].lower())
print(county[-1]) # get the last item 
country_visted = f" i visted {country[3].strip().title()}"
print(country_visted)

# Modifying Elements in a list

country[0] = "Japan"
print(country)

# Adding To the end of a list append()

country.append("Holand")
city=[] # empty list
city.append("Paris")
city.append("Milan")
city.append("Berlin")
print(city)

# instert elements to a list insert()

city.insert(1,"Casablanca") # inserting casabalanca at index number 1

# Removing elements to a list pop() or del 

del country[0]
country.pop() # pop() method the last item on the list
deleted_city = city.pop()
print(deleted_city) 
country.pop(1) # deleting items on the list using index numbers
city.remove("Casablanca") # removing the item using the value 
city_visted = "Paris"
city.remove(city_visted)

# Sorting a list sort()

country.sort()
country.sort(reverse=True) # sort the list reverse 
numbers = [100,2000,3,4,9,1,0,20]
print(numbers.sort())
print(numbers.sort(reverse=True)
numbers.sorted() # sorting the list just Temporarily 

# reverse the Order of a list 
country.reverse()

# lenght of a list
len(numbers)
```











