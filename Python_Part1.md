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
print(name_1.titel()) # title() is method to change eacj word to title case
print(name_1.upper())
print(name_1.lower()) 

job_titel = "manager"
job_titel_1 = "sell"
company = " google"
job = f"{job_titel_1} {job_titel}" # format strings used here to replace the name of any variable in braces {} with its value.
print(job.titel())
print(f" im working as {job.titel()} in this {company.titel()})"

string_with_space = "   mastermind"
string_with_space_1 = "Pentesting    "
print(f"{string_with_space.lstrip()}") # strip the space from the left
print(f"{string_with_space_1.rstrip()}") # strip the space from the right
print(f"{string_with_space.strip()}") # strip the space from the string ( left and right )

number = 10_100_0000_0000_0000 # underscore used to group long numbers to be more readable 
print(number)
number1 , number2 , number3 = 10 , 20 , 30 # Multiple assignment
```




