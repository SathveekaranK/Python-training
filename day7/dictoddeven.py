n={i:"Odd" if i%2==0 else "Even" for i in range(1,11) }
for k,v in n.items():
    print(k,v)