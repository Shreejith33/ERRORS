# Index Error

mylist = [0,1,2,3]
try:
    print(mylist[5])
except IndexError:
    print("Index out of range")

print(mylist[3])
