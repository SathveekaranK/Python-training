try:
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    print(a//b)
except ValueError:
    print("Please enter a valid integer")
except ZeroDivisionError:
    print("Cannot divide by zero")
