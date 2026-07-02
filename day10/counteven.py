arr=[1,2,4,5,6]
k=3
count=0
for c in arr[:k]:
    if(c%2==0):
        count+=1
print(count)
for i in range(k,len(arr)):
    if(arr[i-k]%2==0):
        count-=1
    if(arr[i]%2==0):
        count+=1
    print(count)