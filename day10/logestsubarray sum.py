arr=[1,2,1,0,3]
k=4
win=arr[:1]
t=win[0]
m=len(win)
for i in range(1,len(arr)):
    m=max(m,len(win))
    if(t<=k):
        win.append(arr[i])
        t+=arr[i]
    else:
        t-=win[0]
        win.pop(0)     
print(m)