c0 = int(input("enter the value for collatz's integer : "))
count=0

while c0 > 1 :
    if c0 % 2 == 1 :
        c0 = 3 * c0 + 1
        count+=1
        print(int(c0))
    elif c0 % 2 == 0 :
        c0 = c0 / 2
        count+=1
        print(int(c0))
    else :
        print("error")

print("steps = ",count)