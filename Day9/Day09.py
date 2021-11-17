import json 
import string
letters_alpha = list(string.ascii_lowercase)
def encode(text):
    encoded_word = ""
    list_alpha = []
    try:
        for alpha in text:
            index = letters_alpha.index(alpha)
            letter = letters_alpha[index - 5 ]
            encoded_word += letter
    except ValueError:
        print("{text} contains numbers or symboles ")
    else:

        return encoded_word

def decode(text):
    word = ""
    number = 0
    for letter in text:
        index = letters_alpha.index(letter)
        if (index + 5)  >= 26:
            number = ( index + 5 ) - 26
            word += letters_alpha[number]
        else:
            word += letters_alpha[index + 5 ]

    return word
text = input(" Enter Text To encode ")
filename = "encode.json"
try:
    with open(filename , "w") as f:
        encoded_text = encode(text)
        json.dump(encoded_text, f)
except FileNotFoundError:
    print("File not Found ")
else:
    print(f" {text} Was Encoded And Saved in {filename}")

answer = input(" Would you like to decode your Text ")

if answer == "yes":
    try:
        with open(filename) as f:
            word = json.load(f)
            decoded_word = decode(word)
            print(f"{word} = {decoded_word}")
    except FileNotFoundError:
        print("File Not found ")


