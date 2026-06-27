f=open("day6\helo bro.txt","r")
k=f.read().lower()
v=0
for i in k:
    if i in "aeiou":
        v+=1
print(v)
f.close()
