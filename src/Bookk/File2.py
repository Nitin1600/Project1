from File1 import Calculator

# 1. Create an object
obj = Calculator(10)

# 2. Call methods using the object
print("--- Using Object ---")
obj.add(5)
obj.info()

# 3. Call methods without using the object (using Class name)
print("\n--- Using Class Name ---")
Calculator.info()  # Works fine

try:
    Calculator.add(5)  # Will fail
except Exception as e:
    print(f"Error calling instance method: {e}")

# Key Takeaways:
#
# Instance Method: Requires an object to be created first because it relies on self to access specific data (like self.hostname).
# Class Method: Can be called using either the Class name or the Object. It uses @classmethod and receives cls as the first argument.
# Exception Handling: The try block runs the logic, except catches specific errors, and finally always runs (useful for closing connections or files), regardless of whether an error occurred.
# Calling Instance Method via Class: When you try NetworkDevice.connect(), Python throws a TypeError because it doesn't know which specific device's IP or hostname to use.

# (Q2) Problem 3:
# Execute arcconf getconfig 1 PD Command on a Knox IT/RAID System.
# Redirect that Output to a txt File.
# Write a Python Script, which does the following.
# 1. Read the text File
# 2, Generate a Dictionary whose Key holds Backplane Slot ID and Value is Drive State, for all Drives listed in Output.
#
# arcconf getconfig 1 PD > raid.txt
#
# import re
#
# # Read file and find all Slot IDs and States
# data = open("raid.txt").read()
# slots = re.findall(r"Slot\s+(\d+)", data)
# states = re.findall(r"State\s+:\s+(\w+)", data)
#
# # Combine into a dictionary
# drive_dict = dict(zip(slots, states))
#
# print(drive_dict)

