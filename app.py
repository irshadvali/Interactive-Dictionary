import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def searchYourWord(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no:" % get_close_matches(w,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "N":
             return "The word doesn't exist. Please double check it."
        else:
             return "word doesn't exist in dictionary......"    
    else:
        return "word doesn't exist in dictionary."
    

textWord=input("Enter your word: ")

resultdata=searchYourWord(textWord)

if type(resultdata)==list:
   for item in resultdata:
         print(item)
else:
    print(resultdata)

  