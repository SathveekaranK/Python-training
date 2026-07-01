arr=[2,1,5,1,3,2]
k=3
window_avg=sum(arr[:k])/k
max_avg=window_avg

for i in range(k,len(arr)):
    window_avg=(window_avg*k+ arr[i]-arr[i-k])/k
    max_avg=max(window_avg,max_avg)

print(max_avg)