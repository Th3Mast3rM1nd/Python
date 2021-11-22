file = "./vulnhub.txt"

with open(file) as f:
    data = f.readlines()

newvar = "Healthcare 1: https://www.vulnhub.com/entry/healthcare-1,522/"
for x in data:
    if x.strip() == newvar:
        print("found")
    else:
        print("notfound")
