num=int(input("Enter a number:"))
ans=0
while num >0:
    rem=num%10
    ans=ans*10+rem
    num=num//10

print("The reverse of the number is:", ans)