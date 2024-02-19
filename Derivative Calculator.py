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
def numberCheck2(n):
    number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    num = ""
    if n in number:
        num += n
        return num
    else:
        return "no"
        
def letterCheck(l):
    letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "n", "m", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    let = ""
    if l in letter:
        let += l
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

for i in userInput:
    list.append(symbolsCheck(i))


for i in list:
    if i in number:
        variable = int(i)
    if i in letter:
        constant = 1
print(variable*constant)

