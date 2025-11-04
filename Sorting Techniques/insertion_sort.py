l=[4,1,3,2]
n=len(l)

for i in range(1,n):
    c=l[i]
    p=i-1

    while p>=0 and l[p]>c:
        l[p+1]=l[p]
        p=p-1

    l[p+1]=c

print(l)
