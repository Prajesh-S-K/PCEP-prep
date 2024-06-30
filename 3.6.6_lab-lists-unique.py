my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here.
temp_list=[]
for number in my_list:
    if number not in temp_list :
        temp_list.append(number)
        
my_list=temp_list[:]
#
print("The list with unique elements only:")
print(my_list)
