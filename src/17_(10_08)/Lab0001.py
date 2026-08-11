
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         result=func(*args, **kwargs)
#         return result
#     return wrapper
#
# @decorator
# def add(a, b):
#     print(a + b)
#
# add(2,5)

# def log_operation(func):
#     def wrapper(*args, **kwargs):
#         print("Starting")
#         result = func(*args, **kwargs)
#         print("Ending")
#         return result
#     return wrapper
#
# @log_operation
# def deploy():
#     print("Deploying")
#
# deploy()

# import time
#
#
# def retry(func):
#
#     def wrapper(*args, **kwargs):
#
#         for attempt in range(3):
#
#             try:
#
#                 return func(*args, **kwargs)
#
#             except Exception as error:
#
#                 print(
#                     f"Attempt {attempt + 1} failed: {error}"
#                 )
#
#                 time.sleep(1)
#
#         print("Operation failed")
#
#     return wrapper
#
# @retry
# def connect_to_server():
#
#     print("Connecting to server")
#
#     raise ConnectionError("Server unavailable")
#
# connect_to_server()

# import time
#
# def Timer_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time=time.time()
#         func(*args, **kwargs)
#         end_time=time.time()
#         total_time=end_time - start_time
#         print(f"Total time taken to finish {func.__name__} is {total_time}")
#     return wrapper
#
# def goToLoginPage():
#     print("Please login")
#
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         if isLoggedIn:
#             func(*args, **kwargs)
#         else:
#             goToLoginPage()
#     return wrapper
#
# isLoggedIn=True
#
# @Timer_decorator
# @decorator
# def profile():
#     print("THis is profile page")
#
# @Timer_decorator
# @decorator
# def wishlist():
#     print("THis is whishlist page")
#
# profile()
# wishlist()
