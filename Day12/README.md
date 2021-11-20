# Day 12 

* ***Regular Experssions*** 

[ Check This Link  ](https://github.com/Th3Mast3rM1nd/Linux/blob/master/regular-expressions.md)
```python 
import re
regex = re.compile(r'\d{1,3}(\.\d{1,3}){3}')
matches = regex.search("This is my Ip 192.268.2.2 ")
print(f"Ip Addresse Was found {matches.group()} ")
```
```python
# findall Method 
import re
with open("regx.txt") as f:
    contents = f.read()
regex_ip = re.compile(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.\d{1,3}")
ips = regex_ip.findall(contents)
print(ips)

regex_mails = re.compile(r"[0-9a-z]*[0-9a-z]@[0-9a-z][-\w]*[0-9a-z]\.\w+")
mails = regex_mails.findall(contents , re.I) # flag re.I to Perform case-insensitive matching
print(mails)


