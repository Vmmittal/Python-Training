#Difference between == and === operator
'''== is used to compare the values of two variables but not its data type and  whereas, === compares the both values as well as data types but it is not available in python instead it contains is operator

a=10
b='10'
(a==b) it will retun true,
(a is b) it will return false'''

#if-Else........pass statement

Ram=80
Sham=32
Angad=30

if Ram > Sham :
    if Ram > Angad:
        pass
        # print("Ram is Elder")
    else:
        print("Angad is Elder") 
    print("Pass Executed")       
elif Sham > Angad:
    print("Sham is Elder") 
else:
    print("Angad is Elder")    



#for loop.......
#range(start,end,stepsize) 
# start - index from where we have to start
# end - index untill where we have to go but not include the given end index
# stepsize describes that how many steps we have to skip while iteration)


mycars=["BMW","Audi","Creta","Nexon","Astor"]
print(mycars.__contains__("BMW"))

for x in range(2,11):
    # if(x == 5):
        # break 
     print(x,end=" ")

for x in range(2,10,3):
     print(x) 

for car in mycars:
    if(car == "BMW"):
        continue
    print(car)    




