num = int(input("Enter number: "))
ori = num
rev = 0

while num > 0:
    last = num % 10
    rev = rev * 10 + last
    num = num // 10

if ori == rev:
    print("Palindrome")
else:
    print("Not palindrome")