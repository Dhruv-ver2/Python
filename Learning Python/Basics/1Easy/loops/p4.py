n=int(input("Enter a number:"))

c=0


while n > 0:
    n=n//10
    c+=1

print("The number of digits is:", c)