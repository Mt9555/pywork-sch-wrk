# [ ] create, call and test the str_analysis() function  
def str_analysis(str):
    if str.isalpha(): 
        print(str,'is all alphabetic characters!')
    elif str.isdigit():
        if int(str) > 99:
            print(str,'is a pretty big number!') 
        else:
            print(str,'is a smaller number than expected!')
    else:
            print(str,'has multiple character types!')
str = ''
while str == '' :
    str = input('Enter a string: ')
str_analysis(str) 