# [] create poem mixer
# [] edX assignment page
def word_mixer(word_list):
    word_list.sort()
    new_words = []

    while len(word_list) > 5 :
        new_words.append("\n")
        new_words.append(word_list.pop(-5))
        new_words.append(word_list.pop(0))
        new_words.append(word_list.pop())

    return new_words

user_input = input("Enter a saying:\n")
wordList = user_input.split()
listLength = len(wordList)

for word in range(listLength):
    if len(wordList[word]) <= 3:
        wordList[word] = wordList[word].lower()

    elif len(wordList[word]) >= 7:
        wordList[word] = wordList[word].upper()

    else:
        pass

result = word_mixer(wordList)
for word in result:
    print (word, end=" ")