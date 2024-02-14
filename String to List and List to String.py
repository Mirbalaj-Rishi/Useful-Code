def stringOrIntegerToList(string):
    list = []
    for i in userInput:
        try: #make parts of list integers
            i = int(i)
        except:
            i = str(i)
        list.append(i)
    return list

userInput = input("Please give the string you want to turn to a list: ")
userList = stringOrIntegerToList(userInput)
print(userList)

print("")

def listToString(list):
    string = ""
    for i in list:
        #make parts of list a string
        i = str(i)
        string += i
    return string

print(f"List {userList} to String")
print(listToString(userList))


print("")
# removes zero in front of numbers
def zeroRemover(number):
    number = str(number)
    firstOne = "not yet"
    outPut = ""
    for i in number: #remove zeros in front
        if i != "0" and firstOne == "not yet":
            firstOne = "one has been found"
            outPut += i 
        elif firstOne == "one has been found":
            outPut += i
    outPut = int(outPut)
    return outPut

userNumber = input("please type a number with zeros infront: ")
userNumberNew = zeroRemover(userNumber)
print(userNumberNew)



        
