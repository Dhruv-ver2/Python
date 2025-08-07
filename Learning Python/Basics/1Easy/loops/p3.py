n=int(input("Enter a number:"))

ans=0


while n > 0:
    rem=n%10
    ans=ans+rem
    n=n//10

print("The sum of the digits is:", ans)