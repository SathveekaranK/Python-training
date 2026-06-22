n=[1,2,2,3,3,3,3,3,3,4,2,2]
visited=[]
for i in range(len(n)):
    if n[i] in visited:
        continue
    count=1
    for j in range(i+1,len(n)):
        if(n[i]==n[j]):
            count+=1
    if(count>= len(n)/2):
        print(n[i])
        break
    visited.append(i)

# n=[1,2,2,3,3,3,3,3,3,4,2,2]
# freq={}
# for i in n:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# for j in n:
#     if (freq[j]>= len(n)/2):
#         print(j)
#         break

