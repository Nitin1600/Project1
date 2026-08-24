# 1.What is a function?
# :A function is a reusable block of code that performs a specific task.
# eg:
# def greet():
#     print("Hello")
# greet()

# 2.Why do we use functions?
# :We use functions in Python (and in programming in general) because they make our code easier to write, read, and maintain.
#
# Here’s why functions are important:
#
# > Reusability
# You write the code once and use it many times.
# Example: A function to check warranty can be used for 10 products without rewriting the logic.
# > Better Organization
# Functions break a big program into smaller, logical parts.
# This makes the code easier to understand.
# > Avoid Repetition
# Without functions, you might copy-paste the same code in multiple places.
# Functions help you avoid duplicate code.
# > Easier Debugging
# If something goes wrong, you only need to fix the function, not every place where the code is used.
# > Improves Collaboration
# In team projects, different people can work on different functions without interfering with each other.

# 3.What are the advantages of functions?
# :Code Reusability
# Write once, use many times.
# Avoids rewriting the same logic in multiple places.
# 2. Better Code Organization
# Breaks a large program into smaller, manageable parts.
# Makes the program easier to read and understand.
# 3. Easier Maintenance
# If you need to change the logic, you only update the function — changes apply everywhere it’s used.
# 4. Avoids Code Duplication
# Reduces repeated code, which lowers the chance of errors.
# 5. Easier Debugging & Testing
# You can test functions individually to ensure they work correctly before integrating them into the main program.
# 6. Improves Collaboration
# In team projects, different developers can work on different functions without interfering with each other’s code.
# 7. Supports Modularity
# Functions make it easy to reuse code across different projects or files.
# 💡 Example:
# In your warranty program, if you put the warranty check inside a function, you can:
#
# Use it for any number of products.
# Change the warranty logic in one place instead of everywhere in the code.

# 4.How do you define a function in Python?
# :In Python, you define a function using the def keyword, followed by:
#
# Function name (must follow variable naming rules)
# Parentheses () — can contain parameters (inputs)
# Colon :
# Indented block — the code that runs when the function is called
# (Optional) return statement — sends a value back to the caller
# eg:
# def add_numbers(a, b):
#     return a + b
#
# result = add_numbers(5, 3)
# print("Sum:", result)

# 5.How do you call a function?
# :In Python, calling a function means telling Python to execute the code inside that function.
#
# You call a function by:
#
# Writing its name.
# Adding parentheses ().
# Passing any arguments (if the function requires them) inside the parentheses.
# eg:
# def add_numbers(a, b):
# #     return a + b
# #
# # result = add_numbers(5, 3)
# # print("Sum:", result)
#
# eg:
# # def greet():
# #     print("Hello")
# # greet()

# 6.What is the difference between a function definition and a function call?
# The difference between a function definition and a function call in Python is:
#
# : Function Definition
# What it is:
# Writing the code that describes what the function will do.
# Purpose:
# To create the function and give it a name, parameters, and a body of code.
# When it happens:
# Before you can use (call) the function.
# Keyword used:
# def
# Example:
# def greet_user(name):
#     print(f"Hello, {name}!")
# Here, we defined a function called greet_user that takes one parameter (name) and prints a greeting.
#
# : Function Call
# What it is:
# Telling Python to execute the code inside the function.
# Purpose:
# To run the function’s instructions and (optionally) get a result.
# When it happens:
# After the function has been defined.
# Syntax:
# function_name(arguments)
# Example:
#
# greet_user("Alice")
# Here, we called the function greet_user and passed "Alice" as the argument, so it runs and prints:
#
# Output:
# Hello, Alice!

# 7.What is a parameter?
# :A parameter in Python is a variable that you put inside a function’s parentheses when you define the function.
# It acts as a placeholder for the value you will pass to the function when you call it.
#
# Key Points About Parameters
# They are defined in the function definition.
# They receive values (called arguments) when the function is called.
# They allow you to make functions flexible and work with different data.
# Example:
# # Function definition with a parameter 'name'
# def greet_user(name):
#     print(f"Hello, {name}!")
#
# # Function calls with arguments
# greet_user("Alice")   # 'name' becomes "Alice"
# greet_user("Bob")     # 'name' becomes "Bob"
# Output:
# Hello, Alice!
# Hello, Bob!
# Here:
#
# name → parameter (in the definition)
# "Alice" and "Bob" → arguments (in the calls)
# Parameters vs Arguments
# Term	When Used	Example
# Parameter	In the function definition	def greet_user(name):
# Argument	In the function call	greet_user("Alice")

# 8.What is an argument?
# :An argument in Python is the actual value you pass to a function’s parameter when you call the function.
# It’s the real data that gets sent into the function so it can do its job.
#
# Key Points About Arguments
# They are provided when calling the function.
# They match the parameters defined in the function.
# The number and order of arguments usually must match the parameters (unless you use defaults or special syntax like *args).
# Example:
# # Function definition with a parameter 'name'
# def greet_user(name):
#     print(f"Hello, {name}!")
#
# # Function calls with arguments
# greet_user("Alice")   # "Alice" is the argument
# greet_user("Bob")     # "Bob" is the argument
# Output:
# Hello, Alice!
# Hello, Bob!

# 9.What is the difference between a parameter and an argument?
# :Here’s the clear difference between a parameter and an argument in Python:
#
# :Parameter
# Definition: A variable in the function definition that acts as a placeholder for data.
# Purpose: To receive values when the function is called.
# Where it appears: Inside the parentheses of the function definition.
# When it exists: Before the function runs — it’s part of the function’s blueprint.
# Example:
# def greet_user(name):  # 'name' is a parameter
#     print(f"Hello, {name}!")
# :Argument
# Definition: The actual value you pass to the function when calling it.
# Purpose: To provide real data for the function to work with.
# Where it appears: Inside the parentheses of the function call.
# When it exists: At the moment you call the function.
# Example:
# greet_user("Alice")  # "Alice" is an argument

# 10.Can a function have multiple parameters?
# :Yes ✅ — in Python, a function can have multiple parameters.
# This allows you to pass more than one piece of data into the function at the same time.
# eg:
# def calculate_total(price, quantity):
#     total = price * quantity
#     print(f"Total cost: ${total}")
#
# # Calling the function with two arguments
# calculate_total(50, 3)
# calculate_total(20, 5)

# 11.What is the purpose of the return statement?
# :The return statement in Python is used to send a value back from a function to the place where the function was called.
#
# Purpose of return
# Give back results
#
# Allows a function to produce an output that can be stored in a variable or used in further calculations.
# End function execution
#
# When Python encounters return, it immediately exits the function (no further code in that function runs).
# Enable reusability
#
# Functions that return values can be used in different contexts, not just for printing.
# eg:
# def add_numbers(a, b):
#     return a + b  # Send the sum back to the caller
#
# result = add_numbers(5, 3)  # Store the returned value
# print("Sum:", result)

# 12.What is the difference between print() and return?
# :Here’s the clear difference between print() and return in Python:
#
# :print()
# Purpose: Displays information on the screen (console output) for the user to see.
# Effect: Does not give data back to the caller — it just shows it.
# Use case: For debugging or showing results to the user.
# Return value: Always returns None (even though it displays text).
# Example:
# def greet():
#     print("Hello!")  # Just displays text
#
# result = greet()
# print("Function returned:", result)
# Output:
# Hello!
# Function returned: None
# :return
# Purpose: Sends a value back to the place where the function was called.
# Effect: Ends the function immediately and hands back data.
# Use case: When you need to store, reuse, or process the result later.
# Return value: Whatever you specify after return.
# Example:
# def greet():
#     return "Hello!"  # Sends value back
#
# result = greet()
# print("Function returned:", result)
# Output:
# Function returned: Hello!

# 13.What happens if a function does not have a return statement?
# :If a function in Python does not have a return statement, it will automatically return None after it finishes running.
# This is true even if the function uses print() to display something — printing does not count as returning a value.
#
# Example 1 — No return
# def greet():
#     print("Hello!")  # Only prints, no return
#
# result = greet()
# print("Function returned:", result)
# Output:
# Hello!
# Function returned: None

# 14.Can a function return multiple values?
# Yes ✅ — in Python, a function can return multiple values.
#
# Technically, Python returns them as a tuple, but you can unpack them into separate variables when calling the function.
#
# Example 1 — Returning Multiple Values
# def get_product_info():
#     name = "Laptop"
#     price = 1200
#     warranty_years = 2
#     return name, price, warranty_years  # Multiple values
#
# # Unpacking the returned tuple
# product_name, product_price, product_warranty = get_product_info()
#
# print("Name:", product_name)
# print("Price:", product_price)
# print("Warranty (years):", product_warranty)
# Output:
# Name: Laptop
# Price: 1200
# Warranty (years): 2

# 15.How does Python return multiple values?
:In Python, when a function returns multiple values, it actually returns them as a single tuple — a collection of values grouped together.
The tuple packing happens automatically when you use commas in the return statement, and tuple unpacking happens when you assign the result to multiple variables.

How It Works
1. Tuple Packing (Inside the Function)
2.Tuple Unpacking.
eg:

def get_coordinates():
    x = 10
    y = 20
    z = 30
    return x, y, z  # Tuple packing happens here

# Tuple unpacking happens here
x_coord, y_coord, z_coord = get_coordinates()

print("X:", x_coord)
print("Y:", y_coord)
print("Z:", z_coord)

# 16.Can one function call another function?
# :Yes ✅ — in Python, one function can call another function.
# This is called function composition and is very common in programming to keep code modular and reusable.
#
# How It Works
# You define multiple functions.
# One function can invoke (call) another by using its name followed by parentheses ().
# The called function can return a value that the calling function can use.
# eg:
# def greet(name):
#     return f"Hello, {name}!"
#
# def welcome_user(name):
#     # Calling greet() inside welcome_user()
#     message = greet(name)
#     print(message, "Welcome to our system!")
#
# welcome_user("Alice")

# 17.Can a function be called multiple times?
# :Yes ✅ — in Python, a function can be called multiple times, and each call will execute the function’s code again.
# This is one of the main benefits of functions — you write the code once and reuse it as many times as needed.
# eg:
# def greet_user(name):
#     print(f"Hello, {name}!")
#
# # Calling the function with different arguments
# greet_user("Alice")
# greet_user("Bob")
# greet_user("Charlie")

# 18.What are good function naming conventions?
# :Use lowercase letters with underscores (snake_case).
# Use descriptive names that clearly explain the function’s purpose.
# Start names with verbs if the function performs an action.
# Avoid vague names like do_stuff() or process().
# Avoid unnecessary abbreviations (unless widely known).
# Be consistent with naming style throughout the code.
# Avoid starting names with numbers or special characters.
# If a function returns a value, name it to indicate what it returns (e.g., get_expiry_date).
# If a function performs an action, name it like a command (e.g., print_warranty_status).

# 19.Why are functions important in large projects?
# :Functions are extremely important in large projects because they make code organized, reusable, and easier to maintain.
#
# Here’s a clear, copy-friendly list of reasons:
#
# Code Reusability – Write code once and use it multiple times without rewriting.
# Modularity – Break a big program into smaller, manageable pieces.
# Readability – Makes code easier to read and understand.
# Maintainability – Easier to fix bugs or update specific parts without affecting the whole program.
# Collaboration – Multiple developers can work on different functions without interfering with each other’s code.
# Testing – Functions can be tested individually (unit testing) for correctness.
# Avoids Repetition – Prevents code duplication, reducing errors and saving time.
# Scalability – Easier to expand the project by adding new functions without breaking existing ones.
# Encapsulation – Keeps related logic together, hiding unnecessary details from other parts of the program.
# Improved Debugging – Easier to isolate and fix problems when code is split into functions.

# 20.Give three real-world uses of functions.
# :User Authentication – A function to verify username and password before granting access to a system.
# Data Processing – A function to clean and format raw data before storing it in a database.
# Report Generation – A function to calculate totals, summaries, and generate PDF or Excel reports for business use.

# def authenticate(username, password):
#     return username == "admin" and password == "1234"
#
# print(authenticate("admin", "1234"))  # True
# print(authenticate("user", "pass"))   # False

# def clean_data(text):
#     return text.strip().title()
#
# print(clean_data("   hello world   "))  # "Hello World"

# def generate_report(sales):
#     return f"Total Sales: ${sum(sales)}"
#
# print(generate_report([100, 200, 300]))  # "Total Sales: $600"



