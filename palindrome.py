#Palindrome is solved in two ways. The first method uses slicing and the second method using builtin functions like join and reversed. 

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
