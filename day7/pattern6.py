n=5
p=(n//2)+1
for i in range(1,n+1):
    if(i<p):
        print("*"*i)
    else:
        print("*"*p)
        p-=1