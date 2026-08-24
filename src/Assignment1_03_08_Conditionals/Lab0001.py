# 1.Write a program to check whether a person is eligible to vote (age >= 18).

# age = int(input("Enter age:"))
# if age >=18:
#     print("Eligible")
# else:
#     print("Not Eligible")

# 2.Write a program to check whether a number is positive or negative.

# num=int(input("Enter the number:"))
# if num >= 0:
#     if num > 0:
#         print("Positive")
#     else:
#         print("Zero")
# else:
#     print("Negative")

# 3.Write a program to compare two numbers and display the larger number.

# num1=int(input("Enter the first number:"))
# num2=int(input("Enter the second number:"))
#
# if num1 > num2:
#     print("num1 is greater")
# elif num1 == num2:
#     print("Both numbers are equal")
# else:
#     print("num2 is greater")

# 4.Write a program to check whether two numbers are equal.

# num1=int(input("Enter the first number:"))
# num2=int(input("Enter the second number:"))
#
# if num1 == num2:
#     print("The numbers are equal.")
# else:
#     print("The numbers are not equal.")

# 5.Write a program to determine whether a student has passed (marks >= 35).

# marks = float(input("Enter the marks:"))
#
# if marks>=35:
#     print("passed")
# else:
#     print("Fail")

# 6.Write a program to display "Adult" or "Minor" based on age.

# age = float(input("Enter the marks:"))
#
# if age>=18:
#     print("Adult")
# else:
#     print("Minor")

# 7.Write a program to check whether a password entered matches a predefined password.

# password=input("Enter password:")
# correct_password = "Abc123"
#
# if password==correct_password:
#     print("Matches")
# else:
#     print("Doesn't match")

# 8.Write a program to check whether an item is in stock using a Boolean variable.

# stock=["Apple", "Banana", "Orange", "Grapes"]
# fruit=input("Check the fruit:")
# if fruit:
#     print(f"{fruit} Exists")
# else:
#     print(f"{fruit} is not there")

# Boolean variable indicating stock status
# item_in_stock = True  # Set to False if the item is out of stock
#
# # Function to check stock status
# def check_stock(item_available):
#     if item_available:
#         print("The item is in stock. You can place your order.")
#     else:
#         print("Sorry, the item is out of stock. Please check back later.")
#
# # Example usage
# check_stock(item_in_stock)
#
# # You can also test the out-of-stock scenario
# item_in_stock = False
# check_stock(item_in_stock)

# 9.Write a program to check whether an employee is eligible for a bonus based on years of experience (>= 5 years).
# def check_bonus_eligibility(years_of_experience):
#     if years_of_experience < 0:
#         return "Invalid input. Years of experience cannot be negative."
#     elif years_of_experience >= 5:
#         return "Employee is eligible for a bonus."
#     else:
#         return "Employee is not eligible for a bonus."
# try:
#     years = float(input("Enter the employee's years of experience: "))
#     result = check_bonus_eligibility(years)
#     print(result)
# except ValueError:
#     print("Invalid input. Please enter a valid number.")

# 10.Write a program to check whether a customer gets free delivery based on the purchase amount (>= 1000).
# purchase_amount = float(input("Enter the purchase amount: "))
#
#
# if purchase_amount >= 1000:
#     print("Congratulations! You get free delivery.")
# else:
#     print("Sorry, you do not qualify for free delivery.")

# 11.Write a program to find the largest of three numbers using if...elif...else.
# def find_largest(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
#
#
# # Example usage
# if __name__ == "__main__":
#     # Input three numbers from the user
#     try:
#         num1 = float(input("Enter the first number: "))
#         num2 = float(input("Enter the second number: "))
#         num3 = float(input("Enter the third number: "))
#
#         # Find and print the largest number
#         largest = find_largest(num1, num2, num3)
#         print(f"The largest number is: {largest}")
#
#     except ValueError:
#         print("Please enter valid numbers.")
# The snippet if __name__ == '__main__': allows code to run only when the script is executed directly.
# Ideal for writing modular, reusable, and testable Python code.

# 12.Write a program to assign grades:
#
# A: 90 and above
# B: 75--89
# C: 50--74
# F: Below 50
# def assign_grade(score):
#     if score >= 90:
#         return 'A'
#     elif 75 <= score <= 89:
#         return 'B'
#     elif 50 <= score <= 74:
#         return 'C'
#     else:
#         return 'F'
# def main():
#     try:
#         score = float(input("Enter the student's score: "))
#         if score < 0 or score > 100:
#             print("Invalid score. Please enter a value between 0 and 100.")
#         else:
#             grade = assign_grade(score)
#             print(f"The grade is: {grade}")
#     except ValueError:
#         print("Invalid input. Please enter a numeric value.")
#
# if __name__ == "__main__":
#     main()

# 13.Write a program to classify a person's age as Child, Teenager, Adult, or Senior Citizen.
# def classify_age(age):
#     """
#     Classifies age into categories:
#     - Child: 0-12 years
#     - Teenager: 13-19 years
#     - Adult: 20-59 years
#     - Senior Citizen: 60+ years
#     """
#     if age < 0:
#         return "Invalid age. Age cannot be negative."
#     elif age <= 12:
#         return "Child"
#     elif age <= 19:
#         return "Teenager"
#     elif age <= 59:
#         return "Adult"
#     else:
#         return "Senior Citizen"
#
# def main():
#     try:
#         # Ask user to input age
#         age_input = input("Enter your age: ")
#         age = int(age_input)
#         classification = classify_age(age)
#         print(f"Your age category is: {classification}")
#     except ValueError:
#         print("Invalid input. Please enter a numeric age.")
#
# if __name__ == "__main__":
#     main()

# 14.Write a program to check whether a user can log in using two conditions:
# Correct username
# Correct password
# Predefined
# correct
# username and password
# CORRECT_USERNAME = "admin"
# CORRECT_PASSWORD = "SecurePass123"
#
#
# def login():
#     # Prompt user for username and password
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")
#
#     # Check both username and password
#     if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
#         print("Login successful! Welcome,", username)
#     elif username != CORRECT_USERNAME and password != CORRECT_PASSWORD:
#         print("Invalid username and password. Please try again.")
#     elif username != CORRECT_USERNAME:
#         print("Invalid username. Please try again.")
#     else:  # password is incorrect
#         print("Invalid password. Please try again.")
#
#
# # Example usage
# if __name__ == "__main__":
#     login()

# 15.Write a program to check loan eligibility based on:
# Age >= 21
# Salary >= 30000
# from datetime import datetime
#
# # Input
# dob = input("Enter your date of birth (YYYY-MM-DD): ")
# salary_input = input("Enter your monthly salary: ")
#
# try:
#     birth_date = datetime.strptime(dob, "%Y-%m-%d")
#     age = (datetime.today() - datetime.strptime(dob, "%Y-%m-%d")).days // 365
#     salary = float(salary_input)
#
#     # Eligibility check
#     if age >= 21 and salary > 30000:
#         print(f"You are {age} years old with a salary of {salary}. You are eligible for the loan.")
#     else:
#         reasons = []
#         if age < 21:
#             reasons.append("age")
#         if salary <= 30000:
#             reasons.append("salary")
#         print(f"You are {age} years old with a salary of {salary}. Sorry, you are not eligible due to {' and '.join(reasons)}.")
#
# except ValueError:
#     print("Invalid input. Please ensure date is YYYY-MM-DD and salary is numeric.")

# 16.Write a program to check whether a person can apply for a driving license.
# def check_driving_eligibility(age: int) -> str:
#     """
#     Check if a person can apply for a driving license.
#
#     Args:
#     age (int): Age of the person
#
#     Returns:
#     str: Eligibility status message
#     """
#     if age < 0:
#         return "Invalid age. Age cannot be negative."
#     elif age < 18:
#         return "You are not eligible to apply for a driving license. Minimum age is 18."
#     else:
#         return "Congratulations! You are eligible to apply for a driving license."
#
#
# # Example usage
# if __name__ == "__main__":
#     try:
#         user_age = int(input("Enter your age: "))
#         result = check_driving_eligibility(user_age)
#         print(result)
#     except ValueError:
#         print("Invalid input! Please enter a numeric age.")

# 17.Write a program to determine ticket pricing:
#
# Child
# Adult
# Senior Citizen
# CHILD_PRICE = 5      # Price for children (age < 12)
# ADULT_PRICE = 12     # Price for adults (age 12-59)
# SENIOR_PRICE = 8     # Price for seniors (age 60+)
#
# def get_ticket_count(category):
#     """Helper function to get a valid number of tickets from the user."""
#     while True:
#         try:
#             count = int(input(f"Enter the number of {category} tickets: "))
#             if count < 0:
#                 print("Please enter a non-negative number.")
#             else:
#                 return count
#         except ValueError:
#             print("Invalid input. Please enter an integer.")
#
#
# def calculate_total(children, adults, seniors):
#     """Calculate total ticket cost."""
#     total = (children * CHILD_PRICE) + (adults * ADULT_PRICE) + (seniors * SENIOR_PRICE)
#     return total
#
#
# def result():
#     print("Welcome to the Ticket Pricing Calculator!")
#
#     # Get ticket counts from the user
#     children_count = get_ticket_count("children")
#     adults_count = get_ticket_count("adults")
#     seniors_count = get_ticket_count("senior citizens")
#
#     # Calculate total
#     total_cost = calculate_total(children_count, adults_count, seniors_count)
#
#     # Display results
#     print("- -- Ticket Summary - --")
#     print(f"Children tickets ({children_count} x ${CHILD_PRICE}): ${children_count * CHILD_PRICE}")
#     print(f"Adult tickets ({adults_count} x ${ADULT_PRICE}): ${adults_count * ADULT_PRICE}")
#     print(f"Senior tickets ({seniors_count} x ${SENIOR_PRICE}): ${seniors_count * SENIOR_PRICE}")
#     print(f"Total cost: ${total_cost}")
#
# if __name__ == "__main__":
#         result()

# 18.Write a program to assign a performance rating:
# Excellent
# Good
# Average
# Needs Improvement
# def assign_performance_rating(score):
#     """
#     This function assigns a performance rating based on the score.
#     Scores are assumed to be between 0 and 100.
#     """
#     if score >= 90 and score <= 100:
#         return "Excellent"
#     elif score >= 75 and score < 90:
#         return "Good"
#     elif score >= 50 and score < 75:
#         return "Average"
#     elif score >= 0 and score < 50:
#         return "Needs Improvement"
#     else:
#         return "Invalid score"
#
# # Example Usage
# if __name__ == "__main__":
#     try:
#         score = float(input("Enter the employee's score (0-100): "))
#         rating = assign_performance_rating(score)
#         print(f"Performance Rating: {rating}")
#     except ValueError:
#         print("Please enter a valid numeric score.")

# 19.Write a program to determine the shipping category based on package weight.
# def determine_shipping_category(weight):
#     """
#     Determines shipping category based on the weight of the package.
#
#     Categories (example):
#       - Light: 0 < weight <= 1 kg
#       - Medium: 1 < weight <= 5 kg
#       - Heavy: 5 < weight <= 20 kg
#       - Oversize: weight > 20 kg
#     """
#     if weight <= 0:
#         return "Invalid weight. Weight must be greater than 0."
#     elif weight <= 1:
#         return "Light"
#     elif weight <= 5:
#         return "Medium"
#     elif weight <= 20:
#         return "Heavy"
#     else:
#         return "Oversize"
#
#
# # Example usage
# if __name__ == "__main__":
#     try:
#         weight_input = float(input("Enter the package weight in kg: "))

# 20.Write a program to determine a discount percentage based on the purchase amount.
# def calculate_discount(amount):
#     if amount < 1000:
#         return 5
#     elif amount < 5000:
#         return 10
#     return 15
#
# try:
#     amount = float(input("Enter the purchase amount: ₹"))
#     if amount < 0:
#         print("Purchase amount cannot be negative.")
#     else:
#         discount = calculate_discount(amount)
#         print(f"Purchase Amount: ₹{amount:.2f}")
#         print(f"Discount: {discount}%")
#         print(f"Amount after Discount: ₹{amount * (1 - discount / 100):.2f}")
# except ValueError:
#     print("Invalid input. Please enter a numeric value.")

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

# 21.Create a nested if program to determine college admission eligibility based on marks and age.
# Hint: Store the applicant's information (name, age, marks, course) in a dictionary.
# applicants = {
#     "Alice": {"age": 18, "marks": 92, "course": "Engineering"},
#     "Bob": {"age": 16, "marks": 85, "course": "Arts"},
#     "Charlie": {"age": 19, "marks": 70, "course": "Science"},
#     "Diana": {"age": 17, "marks": 88, "course": "Commerce"}
# }
#
#
# def check_admission(name):
#     # Step 1: Check if the applicant exists
#     if name in applicants:
#         applicant = applicants[name]
#
#         # Step 2: Check age requirement
#         if applicant['age'] >= 17:
#
#             # Step 3: Determine required marks based on course
#             if applicant['course'] == "Engineering":
#                 required_marks = 90
#             elif applicant['course'] == "Science":
#                 required_marks = 75
#             elif applicant['course'] == "Arts":
#                 required_marks = 60
#             else:
#                 required_marks = 70  # default for other courses
#
#             # Step 4: Check if marks meet requirement
#             if applicant['marks'] >= required_marks:
#                 return f"{name} is Accepted for {applicant['course']}."
#             else:
#                 return f"{name} is Rejected due to insufficient marks."
#         else:
#             return f"{name} is Rejected due to age restriction."
#     else:
#         return f"No record found for {name}."
#
#
# # Example usage
# for student in applicants.keys():
#     result = check_admission(student)
#     print(result)

# 22.Create a nested if program to determine whether an employee receives a promotion based on experience and performance.
# Hint: Store the employee details in a dictionary.
# test_employees = {
#     "Alice": {"exp": 6, "score": 95},
#     "Bob": {"exp": 4, "score": 85},
#     "Charlie": {"exp": 2, "score": 70},
# }
# def check_promotion(exp, score):
#     if exp >= 5:
#         if score >= 90:
#             return "Eligible for immediate promotion"
#         elif score >= 75:
#             return "Consider next cycle"
#         else:
#             return "Needs improvement"
#     else:
#         return "Not eligible yet"
#
# for name, details in test_employees.items():
#     result = check_promotion(details["exp"], details["score"])
#     print(f"{name}: {result}")

# 23.Write a program to determine insurance eligibility using multiple conditions.
# Hint: Store customer information such as age, annual income, and vehicle type in a dictionary.

# def check_eligibility(customer):
#     age = customer['age']
#     has_medical_issue = customer['medical_issue']
#     income = customer['income']
#
#     # Conditions for eligibility
#     if age < 18 or age > 65:
#         return False, "Age criteria not met"
#     elif has_medical_issue:
#         return False, "Medical condition disqualifies eligibility"
#     elif income < 20000:
#         return False, "Income criteria not met"
#     else:
#         return True, "Eligible for insurance"
#
#
# # Sample list of customer details
# customers = [
#     {"name": "Alice", "age": 30, "medical_issue": False, "income": 50000},
#     {"name": "Bob", "age": 17, "medical_issue": False, "income": 30000},
#     {"name": "Charlie", "age": 45, "medical_issue": True, "income": 60000},
#     {"name": "Diana", "age": 50, "medical_issue": False, "income": 15000},
# ]
#
# # Process each customer and display eligibility
# for customer in customers:
#     eligible, reason = check_eligibility(customer)
#     print(f"{customer['name']} - Eligible: {eligible}, Reason: {reason}")

# 24.Write a program to determine scholarship eligibility using marks and annual family income.
# Hint: Store the student's details in a dictionary.
# def check_scholarship_eligibility(marks, family_income):
#     """
#     Determines scholarship eligibility based on:
#     - marks: Percentage of academic marks (0-100)
#     - family_income: Annual family income in INR
#     """
#
#     # Define eligibility criteria
#     # Example criteria:
#     # - Marks >= 85 and family_income <= 500000 : Full Scholarship
#     # - Marks >= 75 and family_income <= 750000 : Partial Scholarship
#     # - Marks < 75 or family_income > 750000 : Not eligible
#     if marks >= 85 and family_income <= 500000:
#         return "Eligible for Full Scholarship"
#     elif marks >= 75 and family_income <= 750000:
#         return "Eligible for Partial Scholarship"
#     else:
#         return "Not Eligible for Scholarship"
#
#
# # Main program
# def main():
#     print("Scholarship Eligibility Checker")
#
#     try:
#         marks = float(input("Enter your marks (0-100): "))
#         family_income = float(input("Enter your annual family income (INR): "))
#
#         # Validate input ranges
#         if not (0 <= marks <= 100):
#             print("Error: Marks should be between 0 and 100.")
#             return
#         if family_income < 0:
#             print("Error: Family income cannot be negative.")
#             return
#
#         # Determine eligibility
#         result = check_scholarship_eligibility(marks, family_income)
#         print("Result: ", result)
#
#     except ValueError:
#         print("Invalid input! Please enter numeric values for marks and income.")
#
# # Run the program
# if __name__ == "__main__":
#     main()

# 25.Write a program to determine the internet plan category based on monthly usage.
# Hint: Store customer details and monthly usage in a dictionary.
# customers = {}
#
# def get_plan_category(usage_gb):
#     if usage_gb <= 50:
#         return "Basic Plan"
#     elif usage_gb <= 100:
#         return "Standard Plan"
#     elif usage_gb <= 200:
#         return "Premium Plan"
#     else:
#         return "Unlimited Plan"
#
# def add_customer(name, usage_gb):
#     category = get_plan_category(usage_gb)
#     # Store customer details in the dictionary
#     customers[name] = {"Usage (GB)": usage_gb, "Plan": category}
#     print(f"{name} has been assigned to the '{category}' based on {usage_gb} GB usage.")
#
# add_customer("Alice", 45)  # Basic Plan
# add_customer("Bob", 120)  # Premium Plan
# add_customer("Charlie", 250)  # Unlimited Plan
#
# print("All Customer Details: ")
# for name, details in customers.items():
#     print(f"{name}: {details}")

# or after get_plan_category() functions use below:
# result=get_plan_category(120)
# print(result)

# 26.Write a program to classify electricity usage into different tariff categories.
# Hint: Store the consumer details and electricity consumption in a dictionary.

# def classify_tariff(units):
#     """
#     Classifies electricity usage into tariff categories based on units consumed.
#
#     Tariff categories:
#     - Low: 0-100 units
#     - Medium: 101-300 units
#     - High: 301-500 units
#     - Very High: above 500 units
#     """
#     if units <= 100:
#         return "Low Tariff"
#     elif units <= 300:
#         return "Medium Tariff"
#     elif units <= 500:
#         return "High Tariff"
#     else:
#         return "Very High Tariff"
#
#
# # Store customer details in a dictionary
# customers = {
#     "C001": {"name": "Rajesh", "units_consumed": 75},
#     "C002": {"name": "Anita", "units_consumed": 250},
#     "C003": {"name": "Vikram", "units_consumed": 450},
#     "C004": {"name": "Sonia", "units_consumed": 600}
# }
#
# # Classify and print tariff details for each customer
# for customer_id, details in customers.items():
#     name = details["name"]
#     units = details["units_consumed"]
#     tariff = classify_tariff(units)
#     print(f"Customer ID: {customer_id}, Name: {name}, Units: {units}, Tariff Category: {tariff}")
# Example of adding a new customer dynamically
# new_customer_id = "C005"
# customers[new_customer_id] = {"name": "Amit", "units_consumed": 320}
# print("
# After adding a new customer:")
# name = customers[new_customer_id]["name"]
# units = customers[new_customer_id]["units_consumed"]
# tariff_category = classify_tariff(units)
# print(f"Customer ID: {new_customer_id}, Name: {name}, Units: {units}, Tariff Category: {tariff_category}")

# 27.Write a program to determine the income tax slab based on annual income.
# Hint: Store taxpayer details in a dictionary.
# def determine_tax_slab(income):
#     """Function to determine the tax slab for a given annual income."""
#     if income <= 250000:
#         return "No tax (Exempted)"
#     elif income <= 500000:
#         return "5% tax"
#     elif income <= 1000000:
#         return "20% tax"
#     else:
#         return "30% tax"
#
# # List of incomes to process
# income_list = [200000, 400000, 700000, 1200000]
#
# # Dictionary to store results
# tax_results = {}
#
# # Process each income and store in the dictionary
# for income in income_list:
#     tax_results[income] = determine_tax_slab(income)
#
# # Print the dictionary directly
# print(tax_results)

# 28.Write a program to determine the hotel room category based on budget.
# Hint: Store customer details and budget in a dictionary.
# Customer database with budgets
# Customer database with budgets
# customers = {
#     "Alice": {"budget": 1500},
#     "Bob": {"budget": 3500},
#     "Charlie": {"budget": 8000}
# }
#
#
# def determine_room(name):
#     # 1. Simple if: Check if customer exists
#     if name in customers:
#         budget = customers[name]['budget']
#
#         # 2. if...else: Validate budget
#         if budget >= 0:
#
#             # 3. if...elif...else: Determine room category
#             if budget < 2000:
#                 category = "Standard Room"
#             elif budget < 5000:
#                 category = "Deluxe Room"
#             else:
#                 category = "Luxury Suite"
#
#             # 4. Nested if: Suggest premium service for high budgets
#             if category == "Luxury Suite":
#                 if budget > 7000:
#                     note = "Includes Premium Concierge Service"
#                 else:
#                     note = "Standard Luxury Perks"
#             else:
#                 note = "Standard Amenities"
#
#             print(f"Customer: {name} | Budget: ₹{budget} | Category: {category} | Note: {note}")
#         else:
#             print(f"Customer: {name} | Error: Invalid budget.")
#     else:
#         print(f"Customer: {name} not found in records.")
#
#
# # Testing the logic
# for name in ["Alice", "Bob", "Charlie", "David"]:
#     determine_room(name)

# 29.Write a program to determine product warranty eligibility based on purchase year.
# Hint: Store the product details in a dictionary.
# Product database: name as key, year of purchase as value
# products = {
#     "Laptop": 2025,
#     "Smartwatch": 2024,
#     "Desktop": 2022
# }
#
# current_year = 2026
#
#
# def check_warranty(name):
#     # 1. Simple if: Check if product exists in our records
#     if name in products:
#         year = products[name]
#
#         # 2. if...else: Validate the purchase year
#         if year <= current_year:
#
#             # 3. if...elif...else: Determine warranty status based on age
#             age = current_year - year
#             if age == 0:
#                 status = "Under Full Warranty"
#             elif age <= 2:
#                 status = "Under Limited Warranty"
#             else:
#                 status = "Warranty Expired"
#
#             # 4. Nested if: Check for Extended Plan eligibility
#             # Only products still under some form of warranty are evaluated for extensions
#             if status != "Warranty Expired":
#                 if age < 2:
#                     offer = "Eligible for Extended Protection Plan"
#                 else:
#                     offer = "No extensions available"
#             else:
#                 offer = "N/A"
#
#             print(f"Item: {name} | Status: {status} | Offer: {offer}")
#         else:
#             print(f"Error: Purchase year for {name} cannot be in the future.")
#     else:
#         print(f"Product {name} not found in database.")
#
#
# # Testing the logic
# for item in ["Laptop", "Smartwatch", "Desktop", "Camera"]:
#     check_warranty(item)

30.Design your own real-world problem that uses if, if...else, if...elif...else, and nested if. Write the complete Python program.
Hint: Choose the most suitable data structure. A dictionary is recommended if your problem involves storing details about a person, product, employee, customer, or student.
# Student records
students = {
    "Alice": {"score": 95, "level": "Senior"},
    "Bob": {"score": 40, "level": "Junior"},
    "Charlie": {"score": 75, "level": "Senior"}
}


def check_award(name):
    # 1. Simple if: Check if student exists
    if name in students:
        s = students[name]

        # 2. if...else: Did they pass?
        if s['score'] >= 50:

            # 3. if...elif...else: What reward do they get?
            if s['score'] >= 90:
                reward = "Gold Medal"
            elif s['score'] >= 70:
                reward = "Silver Medal"
            else:
                reward = "Certificate"

            # 4. Nested if: Senior students get an extra bonus!
            if s['level'] == "Senior":
                bonus = " + Extra Scholarship"
            else:
                bonus = ""

            print(f"{name} gets: {reward}{bonus}")
        else:
            print(f"{name} did not pass.")

    else:
        print(f"Student {name} not found.")


# Test the program
check_award("Alice")
check_award("Bob")
check_award("Charlie")


