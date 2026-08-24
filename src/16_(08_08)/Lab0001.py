# def increment():
#     global counter
#     counter += 1
# def decrement():
#     global counter
#     counter -= 1
# def operation(opn):
#     if opn == "inc":
#         increment()
#     if opn == "dec":
#         decrement()
# counter=0
# operation("inc")
# operation("inc")
# # operation("dec")
# print(f"Counter={counter}")

# def increment():
#     global counter
#     counter += 1
#     return 100
# def increment_10():
#     global counter
#     counter += 1
#     c=200
#     return c
# counter=0
# out1=increment()
# out2=increment_10()
# print(counter)
# print(out1)
# print(out2)

# def f2():
#     return 100
# def f1():
#     return f2()
# def f3():
#     return f2
# out1=f1()
# out2=f2()
# out3=f3()()
# out4=f2
# out5=f3()
# print(out1)
# print(out2)
# print(out3)
# print(out4)
# print(out5)

# def increment():
#     global counter
#     counter += 1
# counter=0
# print(increment())
# print(type(increment))
# print(counter)

# lst=[200,400,600]
# out=lst.pop()
# print(lst)
# print(out)

# x=print
# x("Hello World")

# def f2():
#     return 100
# def f1():
#     return f2
# out=f1()
# print(out)
# print(out())
# out_1=f1()()
# print(out_1)

# def multiplier(num1):
#     def inner(num2):
#         out=num1 * num2
#         return out
#     return inner
# out1=multiplier(100)
# out2=multiplier(200)
# print(out1)
# print(out1(3))

# def multiplier():
#     num1=2
#     def inner(num2):
#         out=num1*num2
#         return out
#     return inner
# square=multiplier()
# print(square(4))
# print(square(8))

# def multiplier(num1):
#     def inner(num2):
#         out=num1*num2
#         return out
#     return inner(2)
# out1=multiplier(50)
# print(out1)

# def out():
#     def f1():
#         return 100
#     def f2():
#         return f1()
#     def f3():
#         return f2()
#     def f4():
#         return f3()
#     def f5():
#         return f4()
#     return f5
# print(out()()()())

# def multiplier():
#     num1=2
#     def inner(num2):
#         out=num1*num2
#         return out
#     return inner
# square=multiplier()
# print(square(4))
# print(square(8))

# def seq(num1):
#     def inner(num2):
#         out=num1*num2
#         return out
#     return inner
# total=seq(2)
# print(total(10))

# def f1(f2):
#     print("This is first line")
#     f2()
#     print("This is last line")
# def greet():
#     print("Welcome to ITD")
# def square():
#     num=10
#     print(f"Square of {num} is {num*num}")
# f1(square)

