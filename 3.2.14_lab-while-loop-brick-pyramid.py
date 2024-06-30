blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
bricks = 1
height = 0

while blocks :
    if blocks >= bricks :
        height+=1
        blocks-=bricks
        bricks+=1
    else :
        break
        
#	

print("The height of the pyramid:", height)

