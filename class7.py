#JSON Dumps()............
""" 1.If you need the serialized JSON data in your application of further    processing then you can convert it to a native Python string object instead of  writing it in a file.

 2.The json.dumps() returns the JSON string representation of the Python dict"""

#JSON Dump()...........
'''1.To write the JSON response in a file 
  
   2.For example, you have data in a list or dictionary or any Python object, and you want to encode and store it in a file in the form of JSON. '''


#Program..........

def myFun(arg1, **kwargs):
 for key, value in kwargs.items():
  print("%s: %s" % (key, value))

 print(arg1)

myFun("Arguement1" , Name="Vipul",Designation="Trainee",Training="Python")


#output

'''Name: Vipul
   Designation: Trainee
   Training: Python

 Arguement1  
'''

  
lis1=[{"name":"vipul","age":23},{"name":"rohit","age":20},{"name":"Ajit","age":29},{"name":"Kishan","age":19}]




list4=[x.update({"name":"vm"}) for x in lis1] 
print(list4)
print(lis1)

list5=[x["name"] for x in lis1]
print(list5)










