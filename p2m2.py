# [] create list-o-matic
# [] edX assignment page

def list_o_matic(userInput,List):
    if(userInput == ""):
        print(List[len(List)-1]," popped from list")
        List.pop(len(List)-1)
        return
  
    odd = False
    index = -1
    for i in range(0, len(List)):
        if(List[i] == userInput):
            index=i
            odd=True
            break
  
    if(odd == True):
        List.pop(index)
        print("1 instance of ",userInput," removed from list")
    elif(odd == False):
        List.append(userInput)
        print("1 instance of ",userInput," appended to list")
    return

if __name__ == "__main__":
    List = ["cat","goat","dog","lion"]
    while(True):
        print("look at all the animals ",List)
        userInput = str(input("enter the name of a animal: "))

        if(userInput == "quit"):
            break

        list_o_matic(userInput,List)
        if(len(List) == 0):
            break
    print("Have a good day!")