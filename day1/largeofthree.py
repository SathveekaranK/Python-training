a=int(input("Enter number A:"))
b=int(input("Enter number B:"))
c=int(input("Enter number C:"))
if(a==b==c):
    print("All are equal")
elif(a==b or b==c or a==c):
    print("Two numbers are equal")
elif(a>b and a>c):
    print("A is largest")
elif(b>c):
    print("B is largest")
else:
    print("C is largest")