def evenodd(n):
    if(n%2==0):
        print("It is even")
    else:
        print("It is odd")

n=int(input("Enter number: "))
evenodd(n)
eo=lambda n: "It is even" if n%2==0 else "It is odd"
print(eo(n)) 