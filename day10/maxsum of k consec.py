arr=[2,1,5,1,3,2]
k=3
c=0
for i in range(0,len(arr)-k+1):
    j=i+k
    if(c<sum(arr[i:j])):
        c=sum(arr[i:j])
print(c)