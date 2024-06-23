"""
Created by Mirbalaj Rishi
This simple program will take any times written in start time - end time format
and figure out how much time is between them and add mutiple times together with a for loop

for example inputing 9:00 - 1:00 will output 4 hours
"""


from datetime import datetime

def timeDiffence(startTimeString, endTimeString):
    """
    convert the times from strings to date times, and them subtract them 
    returns the change in time
    """
    endTime = datetime.strptime(endTimeString, '%I:%M')
    startTime = datetime.strptime(startTimeString, '%I:%M')
    deltaTime = endTime - startTime
    
    if deltaTime.total_seconds() < 0:
        #add am or pm if the seconds are negative 
        startTimeString = startTimeString + " am"
        endTimeString = endTimeString + " pm"

        endTime = datetime.strptime(endTimeString, '%I:%M %p')
        startTime = datetime.strptime(startTimeString, '%I:%M %p')
        deltaTime = endTime - startTime

    deltaTimeSeconds = deltaTime.total_seconds()
    deltaTimeHours = deltaTimeSeconds / 3600
    return(deltaTimeHours)

def stringSeperate(string):
    string = string.replace(" ","")
    string = string.replace("-"," ")
    string1, string2 = string.split()
    return string1, string2

totalHours = 0
userInput = input("Please type in your hours in start time - end time format: ")
print("Type stop to stop the program")
while(userInput.lower() != "stop"):
    timeStart, timeEnd = stringSeperate(userInput)
    hours = timeDiffence(timeStart,timeEnd)
    totalHours = totalHours + hours
    print("From", timeStart, "to", timeEnd, "that is", hours, "hours")
    print("Total Hours: ", totalHours)
    print("------------------------- Next Time -----------------------------------")
    userInput = input("Please type in your hours in start time - end time format: ")

print("Thank you for using this program.")
print("Total Hours", totalHours)