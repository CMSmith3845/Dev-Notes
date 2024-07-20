#here we are getting the even numbered characters from a string

word = input("Enter Word")
print("Original String is", word)

for letters in word:
    letters = word[::2]
    print("Every second letter is ", letters)