import json
data = json.load(open("data.json"))

def searchYourWord(w):
    if w in data:
        return data[w]
    else:
        return "word is not matching with dictionary"
    

textWord=input("Enter your word: ")
print(searchYourWord(textWord))

  