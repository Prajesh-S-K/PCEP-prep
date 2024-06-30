# Prompt the user to enter a word
# and assign it to the user_word variable.
vowels = ["A","E","I","O","U"]
user_word = str(input("enter a word :"))
user_word = user_word.upper()

for letter in user_word:
    # Complete the body of the for loop.
    if letter in vowels :
        continue
    print(letter)
    
