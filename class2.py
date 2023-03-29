print("Class 2-- Access, add and remove elements from iterable objects")

#Access particular element in a set.........

set1={1,2,3,4,"vm",4}

for x in set1:
    
    print(x)

print(1 in set1)

#Remove and Discard method............
"""Remove is used to remove the element from set and if the element is not present, then it will raise error, whereas discard method will not show any error"""

set2={2,33,44,"vm",75}
# set2.remove(50)
set2.remove(33)
print(set2)

# set2.discard(50)
set2.discard("vm")
print(set2)


#Intersection_update.........
'''It will show the elements which are present in both the sets'''

set3={22,32,43,"vipul",70}
set4={70,12,34,54,"vm",22}
set3.intersection_update(set4)
print(set3)

#Symmetric_difference_update..........
'''It will show all the elemnts except which are common in both the sets'''
set5={22,32,43,"vipul",70}
set6={70,12,34,54,"vm",22}

set5.symmetric_difference_update(set6)
print(set5)

#Symmetric_difference........
'''It will create a new set of all the elemnts except those are common in both'''
set7={22,32,43,"vipul",70}
set8={70,12,34,54,"vm",22}

set9=set7.symmetric_difference(set8)
print(set9)

#Dictionary.......
mydict={
    "name":"vipul",
    "code":592,
    "location":"Haryana"
}
print(mydict)
print(mydict.keys())
'''Copy dictionary using copy() method'''
newdict=mydict.copy() 
print(newdict)
'''Copy dictionary using in-built dict() method'''
dict2=dict(mydict)
print(dict2)

#Tuple........using append method by converting tuple into list

mytup=(34,43,54,"cloudeq",45.65)
print(mytup)
print(mytup[2])
mylis=list(mytup)
mylis[2]=90
mylis.append("VIPUL")
mytup2=tuple(mylis)
print(mytup2)