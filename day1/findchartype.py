n=input("Enter the character:")
val=ord(n)
if(val>=48 and val<=57):
    print("It is a digit")
elif(val>=97 and val<=122):
    print("It is a Lowercase")
elif(val>=65 and val<=90):
    print("It is a Uppercase")
else:
    print("It is a special character")