# [] create Element_Quiz
# [] edX assignment page
import os
cmd = "curl  https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elements1_20.txt"
os.system(cmd)

file = open("elements1_20.txt", "r+")
file.seek(0)
newlist=[]
newLine = file.readline().strip("\n").lower()
while newLine:
    newlist.append(newLine)
    newLine = file.readline().strip("\n").lower()

print("list any 5 of the first 20 elements in the Period table")

element = []
while len(element) < 5:
    inputForElement = input("Enter the name of an element: ")
    if inputForElement in element:
        print(inputForElement+ " was already entered <-- no duplicates allowed ")
    else:
        element.append(inputForElement)

correctResponse=[]
incorrectResponse=[]
for everyElement in element:
    if everyElement in newlist:
        correctResponse.append(everyElement)
    else:
        incorrectResponse.append(everyElement)

result = len(correctResponse)*20
print("\n")
print(str(result)+"% Correct")

rightResponse=[]
for CorrectData in correctResponse:
    result=CorrectData.title()
    rightResponse.append(result)

found=" ".join(rightResponse)
print("Found: "+found)

wrongResponse=[]
for IncorrectData in incorrectResponse:
    result=IncorrectData.title()
    wrongResponse.append(result)
notFound=" ".join(wrongResponse)
print("Not Found: "+notFound)