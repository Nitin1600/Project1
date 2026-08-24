# (1)

# table=int(input("Enter the table:"))
#
# print(f"{table}*1={table*1}")
# print(f"{table}*2={table*2}")
# print(f"{table}*3={table*3}")
# print(f"{table}*4={table*4}")
# print(f"{table}*5={table*5}")
# print(f"{table}*6={table*6}")
# print(f"{table}*7={table*7}")
# print(f"{table}*8={table*8}")
# print(f"{table}*9={table*9}")
# print(f"{table}*10={table*10}")

# (2)

# num1=int(input("Enter the first number:"))
# num2=int(input("Enter the second number:"))
#
# Sum=num1+num2
# print(f"Sum is:{Sum}")
#
# Sub=num1-num2
# print(f"Sub is:{Sub}")
#
# Mul=num1*num2
# print(f"Mul is:{Mul}")
#
# Div=num1/num2
# print(f"Div is:{Div}")
#
# Pow=num1**num2
# print(f"Pow is:{Pow}")
#
# Whole=num1//num2
# print(f"Whole is:{Whole}")
#
# Mod=num1%num2
# print(f"Mod is:{Mod}")

# (3) Theoretical

# (4)

# pi=3.14
# radius=float(input("Enter the radius of the circle:"))
# area=pi*radius**2
# print(f"Area of the circle with radius of {radius} is {area}")

# (5)

# num1 = float(input("Enter the number1:"))
# num2 = float(input("Enter the number2:"))
#
# if num1>num2:
#     print(f"{num1} is greater then {num2}")
# elif num1 < num2:
#     print(f"{num1} is lesser then {num2}")
# else:
#     print(f"{num1} and {num2} are equal")

# (6)

# num=int(input("Enter the number:"))
#
# Square=num**2
# Cube=num**3
#
# print(f"Square of {num} is {Square}")
# print(f"Cube of {num} is {Cube}")

# (7)

# Year=int(input("Enter the year:"))
# if (Year % 4 == 0) and (Year % 100 != 0) or (Year % 400 == 0):
#     print(f"{Year} is a leap year")
# else:
#     print(f"{Year} is not a leap year")

# (8)

# a=float(input("Enter the first side of triangle:"))
# b=float(input("Enter the second side of triangle:"))
# c=float(input("Enter the third side of triangle:"))
#
# if a==b and b==c and a==c:
#     print("Triangle is equvilateral")
# elif a==b!=c or a==c!=b or b==c!=a:
#     print("Triangle is isosceles")
# else:
#     print("Triangle is scalene")

# (9)

# for i in range(1,101,1):
#     if i%3==0 and i%5==0:
#         print("Fizzbuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     else:
#         print(i)

# (10.a)

num=5
# fac=1
# for i in range(1,num+1):
#     fac*=1
# print(fac)

# number=int(input("Enter number to find factorial of:\n"))
# fact=1
#
# while number:
#     fact*=number
#     number-=1
# print(fact)

# def fac(num):
#     if num<0:
#         return 1
#     return num*fac(num-1)
# out=fac(3)
# print(out)

# parameter = "Pramoda"
#
# match parameter:
#     case "Pramod":
#         print("Hi")
#     case "PramoD":
#         print("2")
#     case _:
#         print("Default")

# age = 6
# if age >= 18:
#     print("Eligible")
# else:
#     print("Not eligible")

# list = [2,3,4,5]
# for a in list:

# result = []
# for x in range(20):
#     if x%2 == 0:
#         result.append(x)
# print(result)

# for x in range(20):
#     if x%2 == 0:
#         print(x, ":Even number")
#     else:
#         print(x, ":Odd number")
#
# nums = [1,3,4,7,6]
# for num in nums:
#     if num % 2 == 0:
#         print(num, "is even number")
#     else:
#         print(num, "is odd number")

# num = 4
# if num % 2 == 0:
#     print(num, "is even number")
# else:
#     print(num, "is odd number")

# def discount(PAmount):
#     if PAmount > 10000:
#         return 500
#     else:
#         return 0
# def totalAmount(PAmount):
#     discAmount=discount(PAmount)
#     finalAmount=PAmount-discAmount
#     print(finalAmount)
# totalAmount(11000)