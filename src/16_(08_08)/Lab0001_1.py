# def process_data(data):
#
#     def clean_data():
#         print("Cleaning data")
#
#     clean_data()
#
# process_data([1, 2, 3])

# def create_counter():
#
#     count = 0
#
#     def counter():
#         nonlocal count
#         count += 1
#         return count
#
#     return counter
#
#
# counter = create_counter()
# counter()
# counter()

# print(counter())
# print(counter())
# print(counter())

# def outer():
#
#     def inner():
#         print("Hello")
#
#     return inner
#
#
# def execute(function):
#     function()
#
#
# my_function = outer()
#
# execute(my_function)

# total = 100
#
# def update():
#     global total
#     total = total + 10
#
# update()
#
# print(total)

# def bank_account(initial_balance):
#
#     balance = initial_balance
#
#     def deposit(amount):
#         nonlocal balance
#         balance += amount
#         return balance
#
#     def withdraw(amount):
#         nonlocal balance
#
#         if amount <= balance:
#             balance -= amount
#
#         return balance
#
#     return deposit, withdraw
#
#
# deposit, withdraw = bank_account(1000)
#
# print(deposit(500))
# print(withdraw(200))
# print(withdraw(100))

