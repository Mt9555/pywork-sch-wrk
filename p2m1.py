# [] create words after "G" following the Assignment requirements use of functions, menhods and kwyowrds
# sample quote "Wheresoever you go, go with all your heart" ~ Confucius (551 BC - 479 BC)
# [] edX assignment page

def wordsAfterG():
    quote = input("enter a 1 sentence quote, non-alpha separate words: ")
    result = ""
    for char in quote:
        if char.lower().isalpha():
            result += char.lower()
        else:
            if(len(result) != 0 and result[0]>'g'):
                print(result)
                result = ""
            else:
                result = ""
    if(len(result) != 0 and result[0]>'g'):
        print(result)

wordsAfterG()