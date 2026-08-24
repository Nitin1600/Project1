# Exercise 1:
#
# Question:
# Create a Python dictionary for one server with cimc_ip, host_ip, and controllers.
#
# Goal:
# Learn variables, dictionary usage, and list access.
#
# Hint:
# Use one dictionary and one list inside it.
#
# Expected:
# Print CIMC IP, Host IP, and number of controllers.
#
# Task:
# Write a simple Python script for this.

# Bro - Script for Exercise 1
# Server1 = {
# "CIMC Ip":"10.126.102.43",
# "Host Ip":"10.126.102.108",
# }
# Controllers = ['MRAID1', 'MRAID2', '1', 'MSTOR-RAID']
# print ("CIMC IP : ",  Server1['CIMC Ip'])
# print ("Host IP :",   Server1['Host Ip'])
# print ("Number of controllers :", (len(Controllers)))

# Server1={
#     "CIMC IP":"10.104.253.29",
#     "Host Ip":"10.104.253.35"
# }
# Controllers=["MRAID1", "MRAID2", "1", "MSTOR-RAID"]
# print("CIMC IP:",Server1["CIMC IP"])
# print("Host Ip:",Server1["Host Ip"])
# print("No.of Controllers:", len(Controllers))

# :::::::::::Exercise 2:::::::
#
# Question:
# Check whether a cimc_ip value is IPv4 or IPv6 and print the result.
#
# Goal:
# Learn if-else condition and simple checking in Python.
#
# Hint:
# Look at the format of the IP address and decide which condition to use.
#
# Expected:
# Print the given CIMC IP and print whether it belongs to IPv4 or IPv6.
#
# Task:
# Write a simple Python script for this.

# Script for Exercise 2
# import ipaddress
# def check_ip(ip_str):
#     try:
#         ip = ipaddress.ip_address(ip_str)
#         if ip.version == 4:
#             return "This is IPV4"
#         elif ip.version == 6:
#             return "This is IPv6"
#
#     except ValueError:
#         return "This is invalid IP"
#
# # print("10.104.253.102", check_ip("10.104.253.102"))
# # print("2001:db8::1", check_ip("2001:db8::1"))
# # print("10.1.0", check_ip("10.1.0"))
#
# user_input = input("Enter an IP address: ")
# result = check_ip(user_input)
# print(result)

import ipaddress



# :::::::::::Exercise 3:::::::
#
# Question:
# Create a list of controller names and print each controller one by one.
#
# Goal:
# Learn list usage and for loop.
#
# Hint:
# Store multiple controller names in one variable and use a loop to print them one at a time.
#
# Expected:
# Print each controller name in a separate line.
#
# Task:
# Write a simple Python script for this.

# Exercise 3 Script
#
# Controllers = [ "LBP", "LRP", "PB", "PBP", "ZB", "ZR", "PR", "DPR", "RB", "DRB", "MB", "MR", "MBP"]
# for Controllers in enumerate(Controllers):
# print(Controllers)
#
# O/p
#
# (0, 'LBP')
# (1, 'LRP')
# (2, 'PB')
# (3, 'PBP')
# (4, 'ZB')
# (5, 'ZR')
# (6, 'PR')
# (7, 'DPR')
# (8, 'RB')
# (9, 'DRB')
# (10, 'MB')
# (11, 'MR')
# (12, 'MBP')

# :::::::::::Exercise 4:::::::
# Question:
# Create a Python dictionary for one server and use a loop to print each controller name from the controllers list.
#
# Goal:
# Learn dictionary access together with for loop.
#
# Hint:
# Store the controller names inside a dictionary value, then access that value and loop through it.
#
# Expected:
# Print the server CIMC IP first, then print each controller name one by one.
#
# Task:
# Write a simple Python script for this.
#
#     O / P
#
#     CIMC
#     IP: 10.126
#     .102
#     .104
#     MRAID1
#     MRAID2
#     1
#     MSTOR - RAID

# :::::::::::Exercise 5:::::::
# Question:
# Create a Python function that takes a cimc_ip as input and prints the base URL.
#
# Goal:
# Learn basic function definition, function call, and using input values inside a function.
#
# Hint:
# Define a function using def, pass one value to it, and print the result from inside the function.
#
# Expected:
# Print a base URL like https://10.10.10.20.
#
# Task:
# Write a simple Python script for this.
#
#     Exersice5
#
#
#     def print_url():
#         ip = input("Enter IP address: ")
#
#
#     print(f"https://" + ip)
#
#     print_url()
#
#     O / P
#
#     Enter
#     IP
#     address: 10.126
#     .102
#     .32
#     https: // 10.126
#     .102
#     .32

# ::::::::::Exercise 6:::::::
# Question:
# Create a Python function that takes a cimc_ip as input and returns the base URL, then print that returned value.
#
# Goal:
# Learn function return value and how to store/use the returned result.
#
# Hint:
# Use return inside the function instead of print.
#
# Expected:
# The function should return a value like https://10.10.10.20, and the script should print it.
#
# Task:
# Write a simple Python script for this.
#
#     def print_url():
#         ip = input("Enter IP address: ")
#
#
#     Url = (f"https://" + ip)
#     return Url
#     Url = print_url()
#     print(Url)
#
#     O / p
#     Enter
#     IP
#     address: 10.126
#     .102
#     .11
#     https: // 10.126
#     .102
#     .11

# :::::::::::Exercise 7:::::::
# Question:
# Create a Python script that writes simple test log lines into a text file.
#
# Goal:
# Learn basic file handling and writing data into a file.
#
# Hint:
# Open a file in write mode and use write() to add lines.
#
# Expected:
# A text file should be created with simple log messages like test start, controller check, and test end.
#
# Task:
# Write a simple Python script for this.
#
#     Exercise7
#
#     Mani = open("Mani.txt", "w")
#     Mani.write("Server-Mt_Adams\n")
#     Mani.write("Controllers: MRAID1, MRAID2\n")
#     Mani.write("All are accessible")
#     Mani.close()

# :::::::::::Exercise 8:::::::
# Question:
# Read a log file and print its contents line by line.
#
# Goal:
# Learn basic file reading and using a loop with file data.
#
# Hint:
# Open the file in read mode and print each line one by one.
#
# Expected:
# Read all lines from the file and display them on screen.
#
# Task:
# Write a simple Python script for this.
#
#     EXercise
#     8
#
#     with open('C:/Users/abkoppan/Exercise7.py') as file:
#         content = file.read()
#     print(content)
#
#     O / p
#     Mani = open("Mani.txt", "w")
#     Mani.write("Server-Mt_Adams\n")
#     Mani.write("Controllers: MRAID1, MRAID2\n")
#     Mani.write("All are accessible")
#     Mani.close()

# :::::::::::Exercise 9:::::::
# Question:
# Create a small Python module named server_utils.py with a function get_base_url(cimc_ip). Then create another script that imports this function and uses it.
#
# Goal:
# Learn packages/modules and how to reuse code from another Python file.
#
# Hint:
# Put the function in one file and use import in another file.
#
# Expected:
# The main script should import the function and print the correct base URL for the given CIMC IP.
#
# Task:
# Write two simple Python files for this:
# 1. server_utils.py
# 2. main.py
#
# Exercise 9
#
# server_utils.py
#
# def print_url():
# ip = input("Enter IP address: ")
# Url = (f"https://"+ip)
# return Url
#
# Url = print_url()
# print(Url)
#
# Main.py
#
# from Server_Utils import Url
#
# O/P
#
# Enter IP address: 10.126.102.11
# https://10.126.102.11

# :::::::::::Exercise 10:::::::
# Question:
# Use regular expression in Python to extract the controller number from this log line:
# Controller Security Enabled on Controller : 2
#
# Goal:
# Learn basic regular expressions using re.search() and group().
#
# Hint:
# Import re module and search for the number at the end of the line.
#
# Expected:
# Print the controller number: 2
#
# Task:
# Write a simple Python script for this.
#
# Exercise 10
#
# import re
# txt = "Controller security enabled on controller : 2"
# Number = re.search("2", txt)
# print(Number)
#
# O/p
# <re.Match object; span=(44, 45), match='2'>


# :::::::::::Exercise 11:::::::
# Question:
# Use regular expression in Python to extract the firmware version from this line:
# Firmware Version : 03.01.41.032
#
# Goal:
# Learn how to extract version-like patterns from text using regular expressions.
#
# Hint:
# Import re module and search for the version value after Firmware Version :
#
# Expected:
# Print the firmware version: 03.01.41.032
#
# Task:
# Write a simple Python script for this.

# Exercise 11
#
# import re
#
# txt = "Firmware Version : 03.01.41.032"
# FW = re.search(r"(\d+.\d+.\d+.\d+)", txt)
#
# if FW:
# print(FW.group(1))
#
# O/p
# 03.01.41.032

# ::::::::::Exercise 12:::::::
# Question:
# Create a simple Python class named TestServer with cimc_ip and host_ip as attributes, and a method show_info() to print both values.
#
# Goal:
# Learn basic classes, objects, attributes, and methods.
#
# Hint:
# Create a class using class, initialize values using __init__, and print them using a method.
#
# Expected:
# Create one object and print CIMC IP and Host IP using the object method.
#
# Task:
# Write a simple Python script for this.


