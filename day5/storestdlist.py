# std=[]
# for i in range(0,5):
#     t=[]
#     n=input("Name:")
#     t.append(n)
#     age=int(input("Age:"))
#     t.append(age)
#     mark=int(input("Mark:"))
#     t.append(mark)
#     std+=t
# print(std)

std={}
for i in range(100,102):
    n=input("Name:")
    age=int(input("Age:"))
    mark=int(input("Mark:"))
    std[i]={n,age,mark}
print(std)

#same using tuple,set and dictionary

# std=[]
# n={}
# for i in range(0,2):
    
#     na=input("Name:")
    
#     age=int(input("Age:"))
    
#     mark=int(input("Mark:"))
#     n=na,age,mark
#     std.append(n)
    
# print(std)