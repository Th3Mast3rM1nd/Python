# Day 3

* ***For loop***

```python 
for i in range(1,10): # range()  function will sequence of numbers from 1 to 9 
    print(i) # i == 1 first time the for loop runs till it reach number 9
for j in range(100): # 0 to 99 
    print(j)
for k in range(1,10,2) # k will be 1 , 3 , 5  moving 2 steps 
    print(k)
numbers = list(range(1,100)) # make a list of numbers using range()
print(numbers)
```
```python 
total = []
for x in range(1,100):
  sum = x + 2
  total.append(sum)
print(total)
print(min(total)) # get min number on the total list
print(max(total)) # get max number on the total list
```
```python 
total = [ x+2 for x in range(100) ] # List comprehension
print(total)

```

* ***for loop and Lists***
```python
countries = [ "France" , "morocco" , "italy" , "india" , "germany" ]
for country in countries:
    print(f"{country.title()} , is nice country ")
    print(f"{country.titel()} , Would be Good to visit it \n") # \n new line 
    
```


  
  
