n=int(input())
j=n-1
for i in range(1,n+1):
    print(" "*j,str(i)*i)
    j-=1