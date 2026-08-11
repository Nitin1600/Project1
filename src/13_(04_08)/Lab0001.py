# print("serverA")
# print("serverB")
# print("serverC")
#
# servers = ["serverA", "serverB", "serverC"]
# for server in servers:
#     print(server)

# (Q)Remove Duplicate Characters from a String
# Imput: programming output: progamin

# (Q)Count Word Frequency in a Sentence
# Input: apple banana apple orange banana apple
# output: apple : 3 banana : 2 orange : 1

# my_input="programming"
# seen = set()
# result = ""
#
# # for char in my_input:
# #     if char not in seen:
# #         seen.add(char)
# #         result += char
# # print(result)
# # print(type(result))
# # print(seen)

# words=input("Enter a string:")
# result=""
#
# for char in words:
#     if char not in result:
#         result=result+char
# print(f"{result}")


# text = "apple banana apple orange banana apple"
# Take input from user
# sentence = input("Enter a sentence: ").strip()
#
# # Split into words
# words = sentence.split()
#
# # Dictionary to store word counts
# word_counts = {}
#
# # Count word frequencies manually
# for word in words:
#     if word in word_counts:
#         word_counts[word] += 1
#     else:
#         word_counts[word] = 1
#
# # Display results
# for word, count in word_counts.items():
#     print(f"{word} : {count}")



# for item in [1,2,3]:
#     print(item)

# count=1
#
# while count <= 5:
#     print(count)
#     count += 1

# for i in range(5):
#     if i==2:
#         pass
#     print(i)
#
# for i in range(5):
#     if i == 2:
#         continue
#     print(i)

# for i in range(5):
#     if i == 2:
#         break
#     print(i)

# for sys import exit:
# for i in range(5):
#     if i == 2:
#         exit()
#     print(i)

# for item in "Python":
#     print(item)
#
# for item in [10,20,30]:
#     print(item)
#
# for item in (10,20,30):
#     print(item)
#
# for item in range(5):
#     print(item)

# student={"name":"john", "age":25}
#
# for key in student:
#     print(key)
#
# for key in student.keys():
#     print(key)
#
# for value in student.values():
#     print(value)
#
# for key, value in student.items():
#     print(key,value)

# for item in {10,20,30}:
#     print(item)

# for line in open("open.txt"):
#     print(line.strip())

# for b in b"Python":
#     print(b)

# for b in bytearray(b"Python)"):
#     print(b)

# for index,value in enumerate(["a", "b", "c"]):
#     print(index,value)

# for a,b in zip(["x","y"],[1,2]):
#     print(a,b)

# for item in sorted([3,1,2]):
#     print(item)
#
# for item in reversed([1,2,3]):
#     print(item)

# servers = ["serverA", "serverB", "serverC"]
# for server in servers:
#     print(server)

# server ={
# "hostname": "web-server-01",
#     "ip": "10.0.1.10",
#     "os": "Ubuntu 24.04",
#     "environment": "Production",
#     "owner": "DevOps Team",
#     "region": "ap-south-1",
#     "instance_type": "t3.medium",
#     "status": "Running"
# }
#
# for key,value in server.items():
#     print(key + " : " + value)

# servers=[
#     {"server":"serverA", "status":"Running"},
#     {"server":"serverB", "status":"Running"},
#     {"server":'serverC', "status":"Stopped"},
#     {"server":"serverD", "status":"Running"}
# ]
#
# for server in servers:
#     print(server["server"], server["status"])
#
# print("\nRunning servers")
# for server in servers:
#     if server["status"] == "Running":
#         print(server["server"])

# import os
#
# for file in os.listdir():
#     print(file)

# import os
#
# for file in os.listdir(C:\Users\nitingpa\PycharmProjects\PythonProject4_05_01_2025\.venv\Scripts\python.exe "C:\Users\nitingpa\PycharmProjects\Project1\src\13_(04_08)"):
#     if file.endswith(".py"):
#         print(file)

# import os
# count=0
#
# for file in os.listdir("."):
#     count += 1
#
# print(count)

# states = ["KA", "KE", "AP", "TE", "TN"]
#
# for state in states:
#     print(state.lower(), end=' ')

# count=0
# states = ["KA", "KE", "AP", "TE", "TN"]
# for state in states:
#     count += 1
#     print(count)
#     print(state)
# print()

# profile={
#     "Name":"Virat",
#     "Age":25,
#     "Skills":["batting", "Bowling"]
# }
#
# # # for data in profile:
# #     # print(data)
# #     # print(profile.keys())
# #     # print(profile.values())
# # print(profile.items())
#
# for key,value in profile.items():
#     print(f"The keys are {key} and values are {value}")

# for i,el in enumerate("India"):
#     print(i,el)
    # exit()
# print("hi")

# for i,el in enumerate("India"):
#     print(i,el)
#     if i==3:
#         exit()
# print("Ok")

# for i,el in enumerate("India"):
#     if i > 2:
#         break
#         print(i, el)
# print("Ok")

# servers=[
#     {"name":"serverA", "status":"Running"},
#     {"name":"serverB", "status":"Running"},
#     {"name":'serverC', "status":"Stopped"},
#     {"name":"serverD", "status":"Running"}
# ]
#
# for server in servers:
#     print(server['name'], server['status'])
#     if server['status'] == 'Stopped':
#         continue
#     print(f"Installing software on {server['name']}")

# servers=[
#     {"name":"serverA", "status":"Running"},
#     {"name":"serverB", "status":"Running"},
#     {"name":'serverC', "status":"Stopped"},
#     {"name":"serverD", "status":"Running"}
# ]
#
# for server in servers:
#     # print(server['name'], server['status'])
#     if server['status'] == 'Running':
#         # continue
#         print(f"Installing software on {server['name']}")
# print("Execution completed")

# import os
# # print(os.listdir())
# # for el in os.listdir():
# for artefact in os.listdir():
#     # print(artefact)
#     if artefact.endswith(".py"):
#         print(artefact)

# import os
# import shutil
# print(os.getcwd())

# import os
# print(os.listdir())
# for el in os.listdir():
#     if not el.endswith('py'):
#         print(el)
#         print(os.remove(os.getcwd() + "/" +el))

# import os
# for el in os.listdir(r"C:\Users\nitingpa\PycharmProjects\Project1\src\13_(04_08)"):
#     abs_path=os.path.abspath(os.path.join(r"C:\Users\nitingpa\PycharmProjects\Project1\src\13_(04_08)",el))
#     print(abs_path)
#
# C:\Users\nitingpa\PycharmProjects\Project1\src\13_(04_08)\text1.txt
# C:\\Users\\nitingpa\\PycharmProjects\\Project1\\src\\13_(04_08)\\text1.txt