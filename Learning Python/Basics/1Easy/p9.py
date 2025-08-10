n=int(input("Enter a number:"))
min=max=n

for i in range(1,10):
    n=int(input("Enter a number:"))
    if n<min:
        min=n
    if n>max:
        max=n

print(f"Minimum number is {min}")
print(f"Maximum number is {max}")