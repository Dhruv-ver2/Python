n=int(input("Enter a number:"))
on=n
rev=0

while(n>0):
    r=n%10
    rev=rev*10+r
    n=n//10

if(rev==on):
    print(f"{on} is palindrome")
else:
    print(f"{on} is not palindrome")
