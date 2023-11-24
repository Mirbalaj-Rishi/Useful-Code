print("This program is made by Mirbalaj Rishi")
print("")

# This collects the user's inputs
userInput = input("Please, input your function: ")



# this funion seperates the exponent in the users input by looking for a "^"
# character and combining everything after it into a string
def exponetCheck(e):
    exponet = ""
    if e.find("^") != -1:
        l = e.find("^")
        for i in range(l+1,len(e)):
            exponet += e[i]
    return exponet
         
# this function separates the numbers in a function by combining all integers that are before the ^ sign
def numberCheck2(n):
    number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    num = ""
    for i in n:
        if i == "^" or i == "":
            break
        elif i in number:
            num += i
    if num !="":
        return num
    else:
        return "no"

# this function seperates the variable 
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
        

    

#this takes the number and exponet, and turns them integers to calculated the derivative
exponet = int(exponetCheck(userInput))
number = int(numberCheck2(userInput))
variable = letterCheck(userInput)
totalNumber = exponet*number
newExponet = exponet - 1

#this prints out the final derivative
print(str(totalNumber)+variable+"^"+str(newExponet))




