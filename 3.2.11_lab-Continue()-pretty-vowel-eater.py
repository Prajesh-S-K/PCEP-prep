word_without_vowels = ""

# Prompt the user to enter a word
# and assign it to the user_word variable.
vowels = ["A","E","I","O","U"]
user_word = str(input("enter a word :"))
user_word = user_word.upper()
word_without_vowels = ""

for letter in user_word:
    # Complete the body of the loop.
    if letter in vowels :
        continue
    word_without_vowels+=letter
    
# Print the word assigned to word_without_vowels.
print(word_without_vowels)
