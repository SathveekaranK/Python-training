n=input("Enter the password:")
class WeakPassError(Exception):
    pass
try:
    if(len(n)<8):
        raise WeakPassError("Password length not enough")
    print("Password updated succesfully")
except WeakPassError as e:
    print(e)