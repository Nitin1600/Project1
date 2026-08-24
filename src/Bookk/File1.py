# Basic OOPS Program :
#
# Python File-1 :
#
# - Define a Class with Constructor, One instance method and one class method
# - Instance Variables to be defined from constructor
# - Write some code inside Instance Method and Class Methods. Use Exception handling - try, except and finally blocks
#
# Python File-2 :
#
# - Import the Python file 1
# - Create an object for Class in Python File 1
# - Using object, call Instance Method and Class Method defined in Class in Python File 1
# - Without using object, try calling Instance Method and Class Method defined in Class in Python File 1



class Calculator:
    def __init__(self, num):
        self.num = num  # Instance variable

    # Instance Method
    def add(self, value):
        try:
            result = self.num + value
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            print("Instance method finished.")

    # Class Method
    @classmethod
    def info(cls):
        try:
            print("This is a Calculator Class.")
        finally:
            print("Class method finished.")
