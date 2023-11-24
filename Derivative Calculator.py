print("This program is made by Mirbalaj Rishi")
print("")

userInput = input("Please, input your function: ")
list = []
constant = ""
variable = ""
letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "n", "m", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
"""
def numbercheck(n):
    try:
        x = int(n)
        return int(n)
    except:
        x = n
"""


def exponetCheck(e):
    exponet = ""
    if e.find("^") != -1:
        l = e.find("^")
        for i in range(l+1,len(e)):
            exponet += e[i]
    return exponet
        

def numberCheck2(n):
    number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    num = ""
    for i in n: 
        if i in number:
            num += i
    if num !="":
        return num
    else:
        return "no"
        
def letterCheck(l):
    letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "n", "m", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    let = ""
    for i in l:
        if i in letter:
            let += i
    if let !="":
        return let
    else:
        return "no"
        
def symbolsCheck(i):
    if numberCheck2(i)!= "no":
        return numberCheck2(i)
    elif letterCheck(i)!="no":
        return letterCheck(i)
    else:
        return "nothing"
    



orginialList = []

print(exponetCheck(userInput))

list.append(numberCheck2(userInput))
list.append(letterCheck(userInput))

print(numberCheck2(userInput))



