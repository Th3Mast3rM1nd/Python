import  csv
import random
import re
import webbrowser
file = "./Vulnhub.csv"
with open(file) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    boxes = []
    for i in reader:
        boxes.append(i[1])
vuln_boxes = []
for box in range(3,len(boxes)):
    vuln_boxes.append(boxes[box])

def clean_list(name_list):
    clean_list = []
    for box in name_list:
        if box != "":
            clean_list.append(box)

    return clean_list
vulnhub_list = clean_list(vuln_boxes)

file = "./vulnhub.txt"

def pick_random_box(boxes):
    random_number = random.randrange(10, len(boxes))
    return boxes[random_number]

def saving_to_file(text):
    text = f"{text}\n"
    with open(file , "a" ) as f:
        f.write(text)

def read_from_file(text):
    with open(file) as f:
        data = f.readlines()
    for x in data:
        if x == text:
            return False 
        else:
            return True
chosen_box = ""
while True:
    chosen_box = pick_random_box(vulnhub_list)
    if read_from_file(chosen_box) == False:
        continue 
    else:
        print(chosen_box)
        saving_to_file(chosen_box)
        break
def regex_link(text):
    regex = re.compile(r'(https?):\/\/([0-9a-zA-Z][-\w]*[0-9a-zA-Z]\.)+[0-9a-zA-Z]*(\/[0-9a-zA-Z\-?,?]*)+')
    url =  regex.search(text)
    return url.group()

link = regex_link(chosen_box)
answer = input("Open the link yes or no ")
if answer == "yes" :
    webbrowser.open_new(link)
else:
    print(f"Here Is The link {link}")
