n="{[()]}"
l=len(n)
i=0
flag=True
if(l%2==0):
    while(l!=i):
        if(n[i]==n[l-1]):
            print(n[i]==n[l-1])
            flag=False
        i+=1
        l-=1
if flag:
    print("Yes")
else:
    print("No")