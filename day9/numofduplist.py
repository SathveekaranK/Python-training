arr=[1,2,3,3,4,4,5,5,6]
n={}
c=0
for i in arr:
    if(i in n):
        n[i]+=1
    else:
        n[i]=1
for i in n:
    if(n[i]>1):
        c+=1
print(c)