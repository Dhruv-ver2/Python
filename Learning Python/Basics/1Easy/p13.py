import time

a=0;b=1
print(a,b,sep='\t',end='\t')

for i in range(8):
    c=a+b
    print(c,end='\t')
    a=b ; b=c