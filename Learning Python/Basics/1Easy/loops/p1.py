'''i=1
while i<=5:
    if(i==3):
        break
    print(i)
    i=i+1'''

password=" "
i=1
while password!= "python":
    if i>5:
        print("Too many attempts! Access denied.")
        break
    password=input("Enter the password: ")
    i+=1

else:
    print("Access granted!")