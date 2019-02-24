import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def searchYourWord(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        return "Did you mean %s instead?" % get_close_matches(w,data.keys())[0]   
    else:
        return "word is not matching with dictionary"
    

textWord=input("Enter your word: ")
print(searchYourWord(textWord))

  