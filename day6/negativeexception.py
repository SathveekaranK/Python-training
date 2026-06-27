class NegativeError(Exception):
    pass

try:
    n=int(input("Enter a number: "))
    if n<0:
        raise NegativeError("Negative numbers are not allowed")
    print("You entered:",n)
except NegativeError as e:
    print(e)
