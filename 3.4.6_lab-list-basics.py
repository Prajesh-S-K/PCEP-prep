hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
list_length = len(hat_list)
middle = list_length//2
hat_list[middle]=int(input("enter the number to replace the middle of the list : "))
print(hat_list)

# Step 2: write a line of code that removes the last element from the list.
hat_list[-1]=int(input("enter the last digit to replace in the list : "))
print (hat_list)

# Step 3: write a line of code that prints the length of the existing list.
print (len(hat_list))
print(hat_list)

