print("\nAssignment 5\n")


#JSON module..................Dump() method is used to convert an object into pyhton strings. To do so,  we need to import JSON module first

import json
import random

print(random.randint(1,10))  # To get random integer we use randint() method from random module


mylist=[1,2,3,4,"vm",54]   #Python List object
print(type(mylist))

myjson_list=json.dumps(mylist)   #Python JSON String
print(type(myjson_list))  

person={
    "name":"Michael",
    "age": 23,
    "nationality": "Australian",
    "owned_Vehicles":["BMW","Audi","Aston","Ferrari"]
}


"""We can pass 4  arguements inside dumps() method"""
# 1. An object which we need to convert
# 2. indent , give spaces to read and understand it in a eficient manner
# 3. sort_keys , to sort the content alphabetically or numerically
# 4. seperators , it is used to seperate the key values pair to better understanding and readability (",",".","=")


print(type(person))
x=json.dumps(person, indent=4, sort_keys=True, separators=(".","="))
print(x)

# Exception Handling...............................

try:
 print(y)
except ArithmeticError:
 print("An error caught")
except NameError:
 print("Not defined") 
else:
 print("Someting else") 
finally:
 print("This also executed") 


 #To raise an exception we have  to  use raise keyword

num=input("Enter number: ")
print(num)
if not type(num) is int:
#  print("only integers required")
 raise TypeError("Only integers required") 


print("After raising Exception")



#List Comprehension...................To  create a new list from the existing list with a shorter syntax according to the given condition

lis1=[{"name":"vipul","age":23},{"name":"rohit","age":20},{"name":"Ajit","age":29},{"name":"Kishan","age":19}]

list2=[x for x in lis1 if x["age"] > 20]  #with if condition

# for x in lis1:
#  if x["age"] > 20:
#   list2.append(x)

print(list2)  

list3=[x["name"].upper() for x in lis1]  #Without if condition
print(list3)

