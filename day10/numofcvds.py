n="hello bro 5$$"
vow="aeiouAEIOU"
c,v,d,s,spl=0,0,0,0,0
for i in n:
    if(i in vow):
        v+=1
    elif(i.isdigit()):
        d+=1
    elif(i==" "):
        s+=1
    elif(not i.isalpha()):
        spl+=1
    else:
        c+=1
print(f'Vowels: {v} \nConsonants: {c} \nDigits: {d} \nSpaces: {s} \nSpecial characters: {spl}')
