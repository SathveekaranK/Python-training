n=8
j=n-2
k=n//2
for i in range(1,n+1):
    if i>=n//2:
        print("*"*k+" "*j+"*"*k)
        j+=2
        k-=1
    else:
        print("*"*i+" "*j+"*"*i)
        j-=2

