l=[4,1,3,2]
n=len(l)

for i in range(n-1):
    swap=False
    for j in range(n-1-i):

        if(l[j]>l[j+1]):
            l[j],l[j+1]=l[j+1],l[j]
            swap=True
    
    if swap==False:
        break
        

print(l)