import  csv
import random
file = "./Hackthebox.csv"
with open(file) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    boxes = []
    for i in reader:
        boxes.append(i[0])
        boxes.append(i[1])
file2 = "./ProvingGround.csv"
with open(file2) as pg:
    reader = csv.reader(pg)
    header_row = next(reader)
    pg_boxes = []
    for i in reader:
        pg_boxes.append(i[0])
        pg_boxes.append(i[1])

# lets get just the boxes for the list 
easy_boxes = []
for i in range(6,len(boxes)):
     easy_boxes.append(boxes[i])
pg_box = []
for i in range(8,len(pg_boxes)):
    pg_box.append(pg_boxes[i])


def clean_list(name_list):
    clean_list = []
    for box in name_list:
        if box != "":
            clean_list.append(box)

    return clean_list

boxes_list = clean_list(easy_boxes)
pg_b = clean_list(pg_box)
def pick_random_box(boxes):
    random_number = random.randrange(10, len(boxes))
    return boxes[random_number]

filename = "./boxes.txt"
def saving_to_file(text):
    text = f"{text}\n"
    with open(filename , "a" ) as f:
        f.write(text)

def read_from_file(text):
    with open(filename) as f:
        data = f.readlines()
    text_list = []
    for i in data:
        text_list.append(i)
    if text not in text_list:
        return True
    else:
        return False
        
        
answer = input("pg or hackthebox ").lower()
while True:
    if answer == "pg":
        pg_today_box = pick_random_box(pg_b).split()
        if read_from_file(pg_today_box) == False:
            continue
        else:
            saving_to_file(pg_today_box)
            break
    if answer == "hackthebox":
        today_box = pick_random_box(boxes_list).split()
        if read_from_file(today_box) == False:
            continue
        else:
            saving_to_file(today_box)
            break



        
        

