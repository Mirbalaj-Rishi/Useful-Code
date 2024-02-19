
# check if carry, if carrey set this number to zero move to next number
#from String to List and List to String File
def stringOrIntegerToList(string):
    list = []
    for i in userInput:
        try: #make parts of list integers
            i = int(i)
        except:
            i = str(i)
        list.append(i)
    return list

def listToString(list):
    string = ""
    for i in list:
        #make parts of list a string
        i = str(i)
        string += i
    return string

def zeroRemover(list):
    firstOne = "not yet"
    newlist = []
    for i in list: #remove zeros in front
        if i != 0 and firstOne == "not yet":
            firstOne = "one has been found"
            newlist.append(i)
        elif firstOne == "one has been found":
            newlist.append(i)
    return newlist
# ---------------------------------

def checkCarry(list):
    carry = "n"
    start = "y" #this stops the list once everything is carried 
    newlist = []
    list.reverse()
    if list[-1] == 1:
        list.append(0)
    for i in list:
        if i == 1 and start == "y":
            newlist.append(0)
            carry = "y"
        elif i == 0 and carry == "y" and start == "y":
            newlist.append(1)
            carry = "n"
            start = "n"
        elif i == 0 and start == "y":
            newlist.append(0)
        # once one is added
        elif start == "n":
            newlist.append(i)
    newlist.reverse()
    return newlist

def binaryAdd(list):
    newList = []
    if list[-1] == 1:
        list = checkCarry(list)
        return zeroRemover(list)
    elif list[-1] == 0:
        list[-1] = 1
        return zeroRemover(list)



userInput = input("Please give the binary number you want to add one too: ")
userList = stringOrIntegerToList(userInput)
userListPlus1 = binaryAdd(userList)
print(userListPlus1)
awnser = listToString(userListPlus1)

print("Here is the binary number you are looking for:", awnser)





            
