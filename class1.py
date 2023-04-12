
"""Stateless nature of rest API's"""

#A Stateless Protocol is a type of network protocol in which a server responds to the client requests based on the current state

"""Status Codes
503 : typically indicates a performance issue on the origin server. 

403 :Forbidden Error,indicates that the server understands the request but refuses to authorize it.

301:  the requested resource has been definitively moved to the URL given by the Location headers."""



"""C  R  U   D   Operations"""

import requests


# POST method 
my_url="https://fakestoreapi.com/products"
my_data={"user_id":1112,"title":"Hello"}
response1=requests.post(my_url,json=my_data)
print(response1)
print(response1.json())


#GET method
my_url="https://jsonplaceholder.typicode.com/todos/1#"
response2=requests.get(my_url)
print(response2)
print(response2.json())


#PUT method
my_url="https://jsonplaceholder.typicode.com/todos/1#"
my_data2={"user_id":1134,"title":"Hello"}
response3=requests.put(my_url,json=my_data2)
print(response3)
# print(response3.json())


#PATCH method
my_url="https://fakestoreapi.com/products/3"
my_data3={"title":"Hello-Vipul"}
response4=requests.patch(my_url,json=my_data3)
# response4=requests.get(my_url)

print(response4)
print(response4.json())


# #DELETE method
my_url2="https://reqres.in/api/users/2"
response5=requests.delete(my_url2)
print(response5)

