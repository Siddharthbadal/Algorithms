word = input("enter a word: ")
newWord = word[::-1]
# if newWord == word:
#     print(True)
#     print(newWord)
# else:
#     print(False)
#     print(newWord)


rev = ''.join(reversed(word))

if word == rev:
    print(True)
else:
    print(False)
