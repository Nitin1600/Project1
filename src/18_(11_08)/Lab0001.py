# file2=open("file1.txt", "w")
# file2.write("\nThis is second line")
# # out=file1.read()
# # print(out)
#
# # out=file1.readlines()
# # print(out)
#
# out=file2.writelines("How you are doing")
# print(out)

# with open("file1.txt", "r") as f:
#     out=f.readlines()
#     lines_less_then_20=[]
#
#     for line in out:
#         if len(line)<20:
#             lines_less_then_20.append(line)
#
# print(lines_less_then_20)

# a,b=10,20
# print(a,b)

# def cube(num):
#     return num ** 3
# list1=[2,3,6,7,9]
# cube_numbers=map(cube,list1)
# print(cube_numbers)
# print(list(cube_numbers))

# def upper_case(data):
#     return data.upper()
# out=list(map(upper_case, "india"))
# print(out)

# nums=[1,4,5,6,78,7,87,99,34]
# out=filter(lambda nums: nums%2, nums)
# print(out)
# print(list(out))

# nums=[1,4,5,6,78,7,87,99,34]
# out=filter(lambda nums: nums%2==0, nums)
# print(out)
# print(list(out))
#
# import functools
# import operator
#
# numbers = [1, 2, 3, 4, 5]
# result = functools.reduce(operator.mul, numbers)
# print(result)  # Output: 120
#
# ((((1*2)*3)*4)*5)

# import requests
# import json
# response=requests.get('https://fakestoreapi.com/products')
# out=response.json()
# # out=response.text()
#
# print(out)
# print(type(out))

# print(out[0])
# print(out[0], keys())
# print(out.get('title'))

# import json
#
# server = {
#     "name": "web-server",
#     "environment": "production"
# }
#
# data = json.dumps(server)
#
# print(data)

# import json
#
# data = '{"name": "web-server", "environment": "production"}'
#
# server = json.loads(data)
#
# print(server)
# print(server["name"])

# import json
#
# server = {
#     "name": "web-server",
#     "environment": "production"
# }
#
# with open("server.json", "w") as file:
#
#     json.dump(server, file, indent=4)

# def is_even(number):
#     return number % 2 == 0
#
# out=is_even(4)
# print(out)

# numbers=[1,2,3,4,5,6,7]
numbers = [10, 20, 5, 30]

# # minimum, maximum, total = analyze(numbers)
# def analyze(numbers):
#     return min(numbers), max(numbers), sum(numbers)
# minimum, maximum, total = analyze(numbers)
# # out=analyze()
# # print(out)
# out=minimum, maximum, total
# print(out)
# print(type(out))
# print(minimum, maximum, total)
# # print(type(minimum, maximum, total))
# print(analyze(numbers))