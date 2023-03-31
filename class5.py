print("Assignment 4")


import os


#Functions in python


'''It is a block of code that is executed when we call it
  We can resue the functions to avoid writing of same lines of code again and again'''

def my_function():
  print("Hello")
my_function()

#program to calculate sum of digits of given number using function and Recursion


number=29
global sum
sum=0

def sum_digits(num,sum):  #function definiton with parameters
  while(num != 0):
   remainder=num%10
   sum=sum + remainder
   num/=10
   
  return sum

result=int(sum_digits(number,sum)) #calling function by passing arguements
print(result)

#using Recursion............

def sum_digits2(num,sum): 
  if num==0:
   return 0

  else:
    remainder=num%10
    sum=remainder + sum_digits2(num/10,0)  #Function calling itself
  return sum

result=int(sum_digits2(1221,sum))
print(result)



#Lambda function...............

func=lambda a : a * 10
print(func(2))

def numbers_list(numbers):
    final_numbers = filter(lambda x: x > 10, numbers)
    return list(final_numbers)



numbers = [1, 22, 3, 432, 53, 64, 7, 8, 9, 10]
result = numbers_list(numbers)
print(result)


#File handling in Python..........

'''TO open a file we use open()'''

f=open("test.txt",'a')
# print(f.read())

# print(f.readline())
# print(f.readline())  #Readline() is used to read one line at a time.

# for x in f:
#   print(x)
# f.close()  
f.write("This is my append mode")
f=open("test.txt")
print(f.read())


# g=open("textfile2.txt","x") # 'x' mode is used to create new file


if os.path.exists("textfile2.txt"):
  os.remove('textfile2.txt')
else:
  print("No such file exist")  



with open("test.txt") as file1:   # with is used to close file automatically
  data=file1.read()
  print(data)