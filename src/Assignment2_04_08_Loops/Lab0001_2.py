# 21.Read marks of multiple students and display Pass/Fail for each student. Hint: Use a dictionary.
# n = int(input("Number of students: "))
# students = {input("Name: "): float(input("Marks: ")) for _ in range(n)}
#
# for name, marks in students.items():
#     print(f"{name}: {'Pass' if marks >= 40 else 'Fail'}")

# 22.Store employee names and salaries. Display employees whose salary is greater than a given amount. Hint: Use a dictionary.
# # Store employee names and salaries
# n = int(input("Number of employees: "))
# employees = {input("Name: "): float(input("Salary: ")) for _ in range(n)}
#
# limit = float(input("Enter salary limit: "))
#
# # Display employees with salary greater than limit
# print(f"Employees earning more than {limit}:")
# for name, salary in employees.items():
#     if salary > limit:
#         print(f"{name}: {salary}")


# 23.Count how many students passed, failed, and received distinction. Hint: Use a dictionary or list.
# # Read student marks and count results
# n = int(input("Number of students: "))
# results = {"Pass": 0, "Fail": 0, "Distinction": 0}
#
# for _ in range(n):
#     marks = float(input("Marks: "))
#     if marks >= 75:
#         results["Distinction"] += 1
#     elif marks >= 40:
#         results["Pass"] += 1
#     else:
#         results["Fail"] += 1
#
# # Display counts
# for category, count in results.items():
#     print(f"{category}: {count}")

# 24.Find duplicate elements in a list. Hint: Use a dictionary to store occurrence counts.
# Find duplicate elements in a list
# items = [4, 2, 7, 4, 9, 2, 1, 7, 3, 3, 4]
#
# counts = {}
# for item in items:
#     counts[item] = counts.get(item, 0) + 1
#
# duplicates = [item for item, count in counts.items() if count > 1]
#
# print("Duplicate elements:", duplicates)



# 25.Find duplicate elements in a list. Hint: Use a dictionary to store occurrence counts.
# # Find duplicate elements in a list
# items = [4, 2, 7, 4, 9, 2, 1, 7, 3, 3, 4]
#
# counts = {}
# for item in items:
#     counts[item] = counts.get(item, 0) + 1
#
# duplicates = [item for item, count in counts.items() if count > 1]
#
# print("Duplicate elements:", duplicates)

# 25.Check whether a string is a palindrome.
# Check if a string is a palindrome
# text = input("Enter a string: ").strip()
#
# if text.lower() == text[::-1].lower():
#     print("Palindrome")
# else:
#     print("Not a palindrome")

# 26.Check whether a number is an Armstrong number.
# Check if a number is an Armstrong number
# num = int(input("Enter a number: "))
# power = len(str(num))  # Number of digits
#
# if num == sum(int(digit) ** power for digit in str(num)):
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")

# 27.Check whether a number is a prime number.
# Check if a number is prime
# num = int(input("Enter a number: "))
#
# if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
#     print("Prime number")
# else:
#     print("Not a prime number")
#
# A prime number is a natural number greater than 1 that has exactly two distinct positive divisors:
#
# 1
# Itself


# 28.Find the factorial of a number.
# num=5
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

# 29.Print the Fibonacci series up to N terms.
# def generate_fibonacci(n):
#     # Handle cases where N is zero or negative
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [0]
#
#     # Initialize series with the first two terms
#     series = [0, 1]
#
#     # Generate subsequent terms
#     while len(series) < n:
#         next_term = series[-1] + series[-2]
#         series.append(next_term)
#
#     return series


# Example usage:
# n_terms = 10
# result = generate_fibonacci(n_terms)
#
# print(f"Fibonacci series for {n_terms} terms: {result}")



# 30.Build a Student Report Card application. Requirements:
#
# Store student details.
# Display total marks.
# Calculate percentage.
# Display grade. Hint: Use a dictionary.
# def generate_report_cards(student_records):
#     print(f"{'Name':<12} | {'Total':<8} | {'Percent':<8} | {'Grade'}")
#     print("-" * 45)
#
#     for name, subjects in student_records.items():
#         total_marks = sum(subjects.values())
#         # Assuming each subject is out of 100
#         percentage = (total_marks / (len(subjects) * 100)) * 100
#
#         # Grading logic
#         if percentage >= 90:
#             grade = 'A'
#         elif percentage >= 80:
#             grade = 'B'
#         elif percentage >= 70:
#             grade = 'C'
#         elif percentage >= 60:
#             grade = 'D'
#         else:
#             grade = 'F'
#
#         print(f"{name:<12} | {total_marks:<8} | {percentage:<8.2f} | {grade}")
#
#
# # Student database
# students = {
#     "Ananya": {"Math": 95, "Science": 88, "English": 92},
#     "Rahul": {"Math": 72, "Science": 65, "English": 70},
#     "Vikram": {"Math": 45, "Science": 50, "English": 55}
# }
#
# # Run the report card generator
# generate_report_cards(students)

# 31.Build a simple ATM menu with:
# Check Balance
# Deposit
# Withdraw
# Exit

def bank_account(initial_balance):

    balance = initial_balance

    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance

    def withdraw(amount):
        nonlocal balance

        if amount <= balance:
            balance -= amount

        return balance

    return deposit, withdraw


deposit, withdraw = bank_account(1000)

print(deposit(500))
print(withdraw(200))
print(withdraw(100))



