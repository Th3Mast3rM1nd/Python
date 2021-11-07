#  password generator " letters Symbols numbers "
import random 
letters = [chr(i) for i in range(97,123)] 
numbers = list(range(0,10))
symbols = ["@","/","-","#","?","!","%"]

password_list  = []
password = ""
for index_letters in range(1,7):
    password_list.append(random.choice(letters))
for index_numbers in range(1,3):
    password_list += str(random.choice(numbers))
for index_symbols in range(1,5):
    password_list += random.choice(symbols)

random.shuffle(password_list)
for key in password_list:
    password += key

print(f" Password = {password}")
