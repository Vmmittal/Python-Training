print("\nAssignment 7\n")

# OOPs in Python Programming

#In this we deal with the concept of objects and classes
#Class is a blueprint which contaiins data member and member function
# Object is an instance of a class

class Cars:
    def __init__(self, color, model,price):   #constructor
        self.color=color
        self.model=model
        self.price=price

    def price_info(self):
        return (f" My car's price is {self.price}")  #declared a function 

 
 #object 1
alto = Cars("white",2017,200000)
print(alto.color + " "+ str(alto.model))

#object 2
swift=Cars("Dark Grey", 2023,300000)
print(swift.color + " "+ str(swift.model))

# object 3
Seltos=Cars("Standard Black", 2022,600000)
print(Seltos.color + " "+ str(Seltos.model))


print(swift.price_info())   #Calling function with an object

# print(swift.checkcheck(20,30))
# swift=Cars()
# print(alto.color)    
# alto.color="Black"
# print(alto.color)

# swift=Cars()
# print(swift.color)



#super() method
"""
1. The super() function is used to give access to methods and properties of a  parent or sibling class.

2. The super() function returns an object that represents the parent class."""

#Class Method
'''The class method in Python is a method, which is bound to the class but not the object of that class.'''