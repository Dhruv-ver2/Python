l=[4,1,3,2]
n=len(l)

for i in range(n):
    m=i

    for j in range(i+1,n):
        if l[j]<l[m]:
            m=j

    l[m],l[i]=l[i],l[m]


print(l)