#Key Error
dictionary = {"fruit":"mango",
              "color":"pink",
              "bird":"sparrow"}
try:
    print(dictionary["bird"])
    print(dictionary["animal"])
except(KeyError):
    print("key animal is not present in dictionary")
    
print(dictionary["fruit"])