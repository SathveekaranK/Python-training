n=5
for i in range(1,n+1):
    j=65
    jj=65
    print(" "*(n-i),end="")
    for j in range(j,j+i):
        print(chr(j),end="")
    for k in range(j-1,jj-1,-1):
        print(chr(k),end="")
    print()