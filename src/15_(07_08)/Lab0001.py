# def append_list(some_data,num):
#     out=some_data.copy()
#     out.append(num)
#     return out
#
# data=[200,400,600]
# output=append_list(data,800)
# print(output)

# def some_func(*args):
#     print(args)
# some_func(10,20,30,40)

# def some_func(**kwargs):
#     print(kwargs)
# some_func(Name='Alice', Age=25)

# def greet():
#     user="Guest"
#     print(f"Welcome {user}")
# greet()
# print(user)

# def greet():
#     print(f"Welcome {user}")
# def some_func():
#     print(f"Welcome {user}")
# user="Guest"
# greet()
# some_func()
# print(user)

# def increment():
#     counter=200
#     print(counter)
# counter=10
# increment()
# print(counter)

# def print_some():
#     print(a)
#     print(b)
#     print(c)
# a,b,c=10,20,30
# print_some()

# def f1():
#     global X
#     X=20
#     print("Inside f1:",X)
#
# def f2():
#     # global X
#     X=30
#     print("Inside f2:",X)
#
# X=100
# print(X)
# f1()
# print(X)
# f2()
# print(X)

# def greet():
#     print("hello")
# greet()

# def add(a,b):
#     return a+b
# result=add(10,20)
# print(result)

# def add(a,b):
#     a=10
#     b=20
#     print(a+b)
# add(100,200)

# def add(a,b):
#     return a+b
# add(10,20)
# add(2,3)
# # add(8)

# def welcome():
#     print("Hi")
# welcome()

# def greet(name):
#     print("Hi",name)
# greet("Barath")

# def add(a,b):
#     print(a+b)
# add(2,3)

# def introduce(name,age):
#     print("Name:",name)
#     print("Age:",age)
# introduce("Rahul",25)
# introduce(25,"Rahul")

# def salary(basics,bonus):
#     return basics+bonus
# result=salary(50000,10000)
# print(result)

# def intro(name,age):
#     print(name)
#     print(age)
# intro(name="Rahul",age=25)
# intro(age=25,name="Rahul")

# def employee(name,age,department):
#     print(name,age,department)
# # employee("Rahul",48,"Devops")
#
# # employee(
# #     name="Rahul",
# #     age=48,
# #     department="Devops"
# # )
# employee(
#     name="Rahul",
#     age=30,
#     department="DevOps"
# )

# def employee(name,age,department):
#     print(name,age,department)
# employee("Rahul",department="Devops",age=25)

# def greet(name="Guest"):
#     print("Hello",name)
# greet()
# greet("Rahul")

# def connect(host,port=80):
#     print("Connecting to", host, "on port", port)
#
# connect("example.com")
# connect("example.com",443)

# def create_user(name, role="user"):
#     print(name,role)
#
# create_user("rahul")
# create_user(name="barath", role="admin")
# create_user()

# def intro(name, message="Hello"):
#     print(name,message)

# def server_config(host,port=22,protocal="ssh"):
#     print(host,port,protocal)
# server_config("10.104.253.29")
# server_config("10.104.253.29",34,"tcp")
# server_config("10.104.253.29",45)
# server_config("10.104.253.29")

# def add(a,b):
#     print("Function")
#     # out= a+b
#     return a+b
# x=10
# y=20
# result=add(2,3)
# print(result)

# def add(a,b):
#     return a+b
# result=add(10+5,10+10)
# print(result)

# def square(x):
#     return x*x
# def add(a,b):
#     return a+b
# result=add(square(2),square(3))
# print(result)

# def display(value):
#     print(value)
# display(10)
# display(10.5)
# display("Hello")
# display([1,1.5,"Hi"])
# display({"name":"Rahul", "age":56})

# def add(a:int, b:int):
#     return a+b
# print(add(10,20))

# def greet(name: str):
#     print("Hello")

# def add(a,b):
#     return a+b
#
# result=add(10,20)
# print(result)

# def add(a,b):
#     print(a+b)
#
# result=add(10,20)
# print(result)

# def add(a,b):
#     return a+b
#
# result=add(10,20)
# print(result)

# def add(a,b):
#     return a+b
#
# result=add(10,20)
# discounted=result-5
# print(discounted)

# def is_even(number):
#     return number % 2 == 0
# def is_even(number):
#     return number % 2 == 0
# if not is_even(3):
#     print("Odd")
# if is_even(10):
#     print("Even")

# def get_status(code):
#     if code==200:
#         return "Success"
#     elif code==400:
#         return "Fail"
#     else:
#         return "Unknown"
# result=get_status(200)
# print(result)

# def get_even_numbers():
#     return [2, 4, 6, 8, 10]
#
# numbers=get_even_numbers()
# for number in numbers:
#     print(number)

# def config():
#     return {
#         "host":"10.104.253.22",
#         "port":22,
#         "protocal":"ssh",
#         "status":"running"
#     }
#
# server=config()
# print(server["status"])
# print(server["port"])

# def get_user():
#     return "Rahul", 30
#
# a,b=get_user()
# print(a)
# print(b)

# def check_age(age):
#     if age >= 18:
#         return "Adult"
#
#     return "Minor"
#
# text1=check_age(19)
# print(text1)

# def test(items):
#     items = [100]
#
# numbers = [1, 2, 3]
#
# out=test(numbers)
# print(out)
#
# print(numbers)

