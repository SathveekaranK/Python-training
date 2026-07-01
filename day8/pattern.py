n=5
j=1
for i in range(n,0,-1):
    if(n==i):
        print("*"*(n*2-1))
    else:
        print("*"*i+" "*j+"*"*i)
        j+=2