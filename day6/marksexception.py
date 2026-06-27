class MarksError(Exception):
    pass

try:
    m=int(input("Enter marks: "))
    if m<0 or m>100:
        raise MarksError("Marks must be between 0 and 100")
    print("Marks: ",m)
except MarksError as e:
    print(e)
