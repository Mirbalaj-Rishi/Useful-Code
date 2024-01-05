"""

This code was made to solve the problem here 
https://open.kattis.com/problems/anewalphabet

It features a conversion function that can change the characters in a string

Made by Mirbalaj Rishi
"""

global list
list = []

global skip
skip = "no"

def conversion(inn, old, new):
    if inn.lower() == old.lower():
        global skip
        skip = "yes"
        list.append(new)
        
        

x = input()

for i in x:
    skip = "no"
    conversion(i,"a","@")
    conversion(i,"b","8")
    conversion(i,"c","(")
    conversion(i,"d","|)")
    conversion(i,"e","3")
    conversion(i,"f","#")
    conversion(i,"n","[]\[]")
    conversion(i,"o","0")
    conversion(i,"p","|D")
    conversion(i,"q","(,)")
    conversion(i,"r","|Z")
    conversion(i,"s","$")
    conversion(i,"g","6")
    conversion(i,"h","[-]")
    conversion(i,"i","|")
    conversion(i,"j","_|")
    conversion(i,"k","|<")
    conversion(i,"l","1")
    conversion(i,"m","[]\/[]")
    conversion(i,"t","']['")
    conversion(i,"u","|_|")
    conversion(i,"v","\/")
    conversion(i,"w","\/\/")
    conversion(i,"x","}{")
    conversion(i,"y","`/")
    conversion(i,"z","2")
    if skip == "no":
        list.append(i)
    



bigString = ""

for i in list:
    c = str(i)
    bigString = bigString + c
print(bigString)
