a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
c=int(input("Enter the third number:"))

if(a==b and b==c):
    print("All three numbers are equal.")
elif(a==b or b==c or a==c):
    print("Two of the numbers are equal.")
else:
    if(a>b):
        if(a>c):
            print("The largest number is:", a)
        else:
            print("The largest number is:", c)
    else:
        if(b>c):
            print("The largest number is:", b)
        else:
            print("The largest number is:", c)