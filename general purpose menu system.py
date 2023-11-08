# general purpose menu system by Mirbalaj Rishi

def mainMenu(Option1, Option2, Option3):
    goodChoice = "no"
    while goodChoice == "no":
        userChoice = input(f"""
Please Input Your Choice
1.{Option1}
2.{Option2}
3.{Option3}

""").lower()
    
        print()
        if userChoice == "1" or userChoice == Option1.lower():
            goodChoice = "yes"
            return Option1
        elif userChoice == "2" or userChoice == Option2.lower():
            goodChoice = "yes"
            return Option2
        elif userChoice == "3" or userChoice == Option3.lower():
            goodChoice = "yes"
            return Option3
        else:
            goodChoice = "no"
            print("please choose one of the options below")


print(mainMenu("first", "second", "third"))
