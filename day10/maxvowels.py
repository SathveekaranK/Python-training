# s="abciiidef"
# k=3
# max_vow=0
# for i in range(k,len(s)):
#     win_res=s[i-k:i]
#     c=0
#     for i in win_res:
#         if i in "aeiou":
#             c+=1
#     if(max_vow<c):
#         max_vow=c
# print(max_vow)

#Sliding window

s="abciiidef"
k=3
vowels="aeiou"
count=0
for c in s[:k]:
    if(c in vowels):
        count+=1
max_count=count

for i in range(k,len(s)):
    if(s[i-k] in vowels):
        count-=1
    if(s[i] in vowels):
        count+=1
    max_count=max(max_count,count)
print(max_count)