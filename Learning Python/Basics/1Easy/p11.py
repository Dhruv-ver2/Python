n=int(input("Enter a number:"))

sum=0

for i in range(1,n+1):
    p=1
    for j in range(1,i+1):
        p=p*j
        print(f"p = {p}")
    
    sum=sum+p

print("Ans = ",sum)