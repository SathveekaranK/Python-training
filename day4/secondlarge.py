n=[3,7,2,9,5]
lar=n[0]
sec=n[0]
for i in n:
    if i>lar:
        sec=lar
        lar=i
    elif i>sec and i!=lar:
        sec=i
print(sec)
