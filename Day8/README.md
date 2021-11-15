# Day 8

* ***Reading from a files*** 

```python 
with open("file.txt") as file_content:
     contents = file_content.read()
print(contents)
```
```python 
file_path = "/home/mastermind/Downloads/numbers.txt"
with open(file_path) as file_content:
     contents = file_content.read()
print(contents)
```
```python
# reading lines 
with open("numbers.txt") as file_content:
     for number in file_content:
         print(number.rstrip())
```
```python 
# making a list from a file
with open("names.txt") as file_content:
     names = file_content.readline()
     
for name in names:
    print(name.rstrip())
```
* ***write to files***
```python 
filename = "numbers.txt"
with open(filename , "w" ) as file_contents:
     for i in range(1,100):
         file_contents.write(f"str(i)\n")
```
* ***appending to files***
```python 
filename = "numbers.txt"
with open(filename , "a" ) as file_contents:
     for x in range(100,1000):
         file_contents.write(f"{str(x)\n")
```
