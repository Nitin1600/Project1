# def greet():
#     print("Hello")
# greet()

# def greet(name):
#     print(name)
# greet("Rahul")

# def add(a,b):
#     print(a+b)
#
# def add(a,b):
#     return(a+b)

# def greet(name):
#     print(name)
# greet("Rahul")

# def values():
#     return 10,20

# numbers=[2,3,4,5,6,7,8,9,10]
# number_sqr=[i*i for i in numbers]
# print(number_sqr)

# numbers=[2,3,4,5,6,7,8,9,10]
# number_sqr2=[]
# for i in numbers:
#     number_sqr2.append(i*i)
# print(number_sqr2)

# numbers=[2,3,4,5,6,7,8,9,10]
# number_sqr3=[i*i for i in numbers if i%2 != 0]
# print(number_sqr3)

# number_sqr4=[]
# numbers=[2,3,4,5,6,7,8,9,10]
# for i in numbers:
#     if i%2 !=0:
#         number_sqr4.append(i*i)
# print(number_sqr4)

# country='india'
# country_list=[i for i in country]
# print(country_list)

# country='india'
# country_list=[]
# for i in country:
#     country_list.append()
# print(country)

# import os
# print(os.listdir())
# print("\n")
# file_others=[f for f in os.listdir() if not f.endswith("py")]
# print(file_others)

# import os
# file_others=[]
# for f in os.listdir():
#     if not f.endswith("py"):
#         file_others.append(f)
# print(file_others)

# counter=0
# # print(counter)
# while counter < 3:
#     counter += 1
#     print(counter)

# counter=0
# something=True
#
# while something:
#     counter += 1
#     print(counter)
    # if counter == 5:
    #     something=False

# numbers=[2,3,4,5,6,7,8,9,10]
# while numbers:
#     out=numbers.pop()
#     # print(out)
#     print(numbers)

# numbers=[]
# counter=0
#
# while numbers:
#         counter += 1
#         numbers.append(counter)
#         print(numbers)
    # if counter==3:
        # break
        # numbers[]
        # numbers.clear()

# print("*"*40)
# print("Welcome to Itd")
# print("*"*40)

# user1="Virat"
# print("*"*40)
# print(f"Welcome {user1} to Itd")
# print("*"*40)
# user2="Kishan"
# user3="Rohith"

# def greet(user):
#     print("\n"*3 + "*"*40)
#     print(f"Welcome {user} to Itd")
#     print("*" * 40)
#
#
# user1="Virat"
# greet(user1)
# user2="Kishan"
# greet(user2)
# user3="Rohith"
# greet(user3)
# greet("Kishan")

# def srt(num):
#     out=num*num
#     print(out)
#
# srt(6)

# def srt(num):
#     out=num*num
#     return "ABCD"
#
# print(srt(6))
# # print(out)
#
# def add(number1, number2):
#     return number1 + number2
# out=add(10,20)
# print(out)

# def add(numbers):
#     out=0
#     for i in numbers:
#         out += i
#     return out
# output=add([10,20,50])
# print(output)

# def maths(num1,num2,operation):
#     out="Give valid input"
#     if operation == "add":
#         out=num1+num2
#     if operation == "sub":
#         out=num1-num2
#     if operation =="mul":
#         out=num1*num2
#     if operation == "div":
#         out=num1/num2
#     return out
#
# output=maths(4,2, "str")
# print(output)

# parameter = "Pramoda"
#
# match parameter:
#     case "Pramod":
#         print("Hi")
#     case "Pramoda":
#         print(2)
#     case _:
#         print("Default")

# while True:
#     text=input("Enter text: \n")
#     out=(text==text[::-1])
#     if out == True:
#         exit()

# states=["Up", "Bihar", "Tn"]
# capitals=["Lucknow", "Patna", "Chennai"]
# out=zip(states,capitals)
# print(dict(out))

