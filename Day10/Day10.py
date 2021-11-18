from os import system, listdir, getcwd

files = listdir(getcwd())

if len(files) == 0:
    print(" No files Was FOund in this Directory")
    exit()
ext = input("Enter The extenstion you want to search for ( .txt , .py , .jpeg , .sh )")
counter = 0
counter1 = 0
files_txt = []
files_other_ext = []
for file in files:
    if file.endswith(ext):
        counter += 1
        files_txt.append(file)
    else:
        counter1 += 1
        files_other_ext.append(file)

print(f" total files was with {ext}  is {counter} ")
print(f" total files was found without txt extenstion {counter1} ")

if counter >= 1:
    answer = input(" WOuld like to see the files yes|y or no|n ")
    if answer == "yes" or answer == "y" :
        for file in files_txt:
            print(file)
    else:
        print(" Program Terminated ")
        exit()
