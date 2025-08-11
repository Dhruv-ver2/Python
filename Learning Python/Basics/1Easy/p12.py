n=int(input("Enter a number:"))

sum,f=0,1

for i in range(1,n+1):
    f*=i
    sum+=f


print(f"The sum of the factorials from (1 to {n}) is {sum}")