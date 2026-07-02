n="{[(])}"
s=["{}","[]","()"]
l=len(n)
i=0
flag=True
if(l%2==0):
    while(l!=i):
        if(n[i]+n[l-1] not in s):
            flag=False
        i+=1
        l-=1
else:
    flag=False
if flag:
    print("Yes")
else:
    print("No")