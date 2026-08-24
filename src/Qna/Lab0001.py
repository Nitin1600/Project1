# (Q):Create a list containing 10 numbers.
# Find the length of a list.
# Access the first, last, and middle element.
# Add an element at the end.
# Insert an element at a specific position.
# Remove an element by value.
# Remove an element using its index.
# Reverse a list.
# Sort a list in ascending order.
# Sort in descending order.

# list_1= [1,2,3,4,5,6,7,8,9,10]
# # len1=len(list_1)
# # print(len1)
# print(list_1[0], list_1[len(list_1)//2], list_1[9],)
# print(list_1[9])
# print(list_1[4])
# list_1.append(11)
# print(list_1)
# list_1[1]=12
# print(list_1)
# list_1.insert(0,13)
# print(list_1)
# list_1.remove(3)
# print(list_1)
# list_1.pop(3)
# print(list_1)
# list_2=list_1[::-1]
# print(list_2)
# list_3=sorted(list_1)
# print(list_3)
# list_4=sorted(list_1, reverse=True)
# print(list_4)


# list_1.reverse()
# list_1.sort()
# list_1.sort(reverse=True)
# print(list_1[0])
# print(list_1[-1])
# print(list_1[len(list_1)//2])

# (Q)Remove Duplicate Characters from a String
# Imput: programming output: progamin

# (Q)Count Word Frequency in a Sentence
# Input: apple banana apple orange banana apple
# output: apple : 3 banana : 2 orange : 1

# words=input("Enter a string:")
# result=""
#
# for char in words:
#     if char not in result:
#         result=result+char
# print(f"{result}")


# text = "apple banana apple orange banana apple"
# sentence = input("Enter a sentence: ").strip()
#
# words = sentence.split()
# word_counts = {}
#
# for word in words:
#     if word in word_counts:
#         word_counts[word] += 1
#     else:
#         word_counts[word] = 1
#
# for word, count in word_counts.items():
#     print(f"{word} : {count}")


# import os
# print(os.getcwd())
# folder_path= "C:\\Users\\nitingpa\\OneDrive - Cisco\\Documents\\Recordings"
# exists =os.path.exists(folder_path)
#
# if exists:
#     print(f'The folder {folder_path} exists.')
# else:
#     print(f'The folder {folder_path} does not exist.')

# import os
#
# print(os.listdir())
# print(os.getcwd())
#
# folder_path = r"C:\Users\nitingpa\PycharmProjects\Project1\src"
#
# if os.path.exists(folder_path):
#     print(f'The folder {folder_path} exists.')
#
#     txt_files = []
#
#     for f in os.listdir(folder_path):
#         if f.lower().endswith(".txt"):
#             txt_files.append(f)
#
#     if txt_files:
#         print("Found .txt files:")
#         for file in txt_files:
#             print(f" - {file}")
#     else:
#         print("No .txt files found in the folder.")
#
# else:
#     print(f'The folder {folder_path} does not exist.')

# import os
# folder="dir1"
# for file in os.listdir(folder):
#     if file.endswith(".log"):
#         out=os.remove(os.path.join(folder, file))
#         print("removed", file)

# 1) Write function for calculator  which can return the output for 2 numbers with kind of operation provided.
# def calculator(a,b,operation):
#     if operation == "add":
#         return a+b
#     elif operation == "sub":
#         return a-b
#     elif operation == "mul":
#         return a*b
#     elif operation == "division":
#         if b == 0:
#             raise ValueError("Cannot divide by zero.")
#         return a / b
#     elif operation == 'power':
#         return a ** b
#     else:
#         raise ValueError(
#             f"Invalid operation: {operation}. Choose from add, subtract, multiply, divide, power.")
# # print(f"Result of {operation} is {result}")
#
# out=calculator(2,3,"add")
# print(out)
#
#
#
#
# 2) Write function that can return repetitive elements .
# def repetitive_elements(numbers):
#
#         element_counts = {}
#         for item in numbers:
#             if item in element_counts:
#                 element_counts[item] += 1
#             else:
#                 element_counts[item] = 1
#         # print(element_counts())
#
#
#         repetitive_elements1 = []
#         for item, count in element_counts.items():
#             if count > 1:
#                 repetitive_elements1.append(item)
#
#         return repetitive_elements1
#
# numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3, 7]
# print("Repetitive elements:", repetitive_elements(numbers))
# print(element_counts(numbers))

numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3, 7]
Count={}
for char in numbers:
    if char in Count:
        Count[char] += 1
    else:
        Count[char] = 1
print(Count)










