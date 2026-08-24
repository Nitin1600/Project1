# 1.Create a Student Report function that accepts name and marks and displays the details.
# def student_report(name, marks):
#     return {
#         "name": name,
#         "marks": marks
#     }
#
# # Example usage
# report = student_report("Alice", 92)
#
# # Display the details
# print(report)
# print("=== Student Report ===")
# print("Name:", report["name"])
# print("Marks:", report["marks"])

# 2.Create a Salary Calculator function that calculates annual salary from monthly salary.
# def salary_calculator(monthly_salary):
#     if monthly_salary < 0:
#         raise ValueError("Monthly salary cannot be negative.")
#
#     annual_salary = monthly_salary * 12
#     return annual_salary
#
#
# # Example usage
# monthly = 5000
# annual = salary_calculator(monthly)
#
# print("Monthly Salary: $", monthly)
# print("Annual Salary: $", annual)

# 3.Create a GST Calculator function.
# def gst_calculator(price, gst_rate):
#     if price < 0 or gst_rate < 0:
#         raise ValueError("Price and GST rate must be non-negative.")
#
#     gst_amount = (price * gst_rate) / 100
#     total_price = price + gst_amount
#     return gst_amount, total_price
#
#
# # Example usage
# gst, total = gst_calculator(1000, 18)
#
# print(f"GST Amount: ₹{gst:.2f}")
# print(f"Total Price: ₹{total:.2f}")

# 4.Create an EMI Calculator function.
# def calculate_emi(principal, annual_rate, years):
#     # 1. Convert annual rate to monthly rate
#     monthly_rate = (annual_rate / 12) / 100
#
#     # 2. Convert years to months
#     months = years * 12
#
#     # 3. Apply the EMI formula
#     # EMI = [P * r * (1 + r)^n] / [(1 + r)^n - 1]
#     emi = (principal * monthly_rate * ((1 + monthly_rate) ** months)) / \
#           (((1 + monthly_rate) ** months) - 1)
#
#     return round(emi, 2)
#
#
# # Example usage
# loan_amount = 500000  # ₹5 Lakhs
# interest = 10.5  # 10.5% annual interest
# tenure = 5  # 5 years
#
# monthly_payment = calculate_emi(loan_amount, interest, tenure)
#
# print(f"Loan Amount: ₹{loan_amount}")
# print(f"Interest Rate: {interest}%")
# print(f"Tenure: {tenure} years")
# print(f"Your Monthly EMI is: ₹{monthly_payment}")

# 5.Create a Rectangle Calculator function that returns area and perimeter.
# def rectangle_calculator(length, width):
#     """
#     Calculate the area and perimeter of a rectangle.
#
#     :param length: Length of the rectangle (float or int)
#     :param width: Width of the rectangle (float or int)
#     :return: Dictionary with area and perimeter
#     """
#     if length <= 0 or width <= 0:
#         raise ValueError("Length and width must be positive numbers.")
#
#     area = length * width
#     perimeter = 2 * (length + width)
#
#     return {
#         "Area": area,
#         "Perimeter": perimeter
#     }
#
# # Example usage
# result = rectangle_calculator(5, 3)
#
# print("=== Rectangle Calculation ===")
# print(f"Area: {result['Area']}")
# print(f"Perimeter: {result['Perimeter']}")

# 6.Create a Circle Calculator function that returns area and circumference.
# import math
#
# def circle_calculator(radius):
#     """
#     Calculate the area and circumference of a circle.
#
#     :param radius: Radius of the circle (float or int)
#     :return: Dictionary with area and circumference
#     """
#     if radius <= 0:
#         raise ValueError("Radius must be a positive number.")
#
#     area = math.pi * radius ** 2
#     circumference = 2 * math.pi * radius
#
#     return {
#         "Area": area,
#         "Circumference": circumference
#     }
#
# # Example usage
# result = circle_calculator(7)
#
# print("=== Circle Calculation ===")
# print(f"Area: {result['Area']:.2f}")
# print(f"Circumference: {result['Circumference']:.2f}")

# 7.Create a Temperature Converter function (Celsius to Fahrenheit).
# def celsius_to_fahrenheit(celsius):
#     """
#     Convert temperature from Celsius to Fahrenheit.
#
#     :param celsius: Temperature in Celsius (float or int)
#     :return: Temperature in Fahrenheit (float)
#     """
#     return (celsius * 9/5) + 32
#
# # Example usage
# temp_c = 25
# temp_f = celsius_to_fahrenheit(temp_c)
# print(f"{temp_c}°C = {temp_f:.2f}°F")

# 8.Create a Currency Converter function using a fixed conversion rate.
# def currency_converter(amount, rate):
#     if amount < 0 or rate <= 0:
#         raise ValueError("Amount must be non-negative and rate must be positive.")
#
#     return amount * rate
#
#
# # Example usage
# usd_to_inr_rate = 83.25  # 1 USD = ₹83.25 (fixed rate)
# usd_amount = 100
# inr_amount = currency_converter(usd_amount, usd_to_inr_rate)
#
# print(f"${usd_amount} USD = ₹{inr_amount:.2f} INR")

# 9.Create an Invoice function that accepts product name, quantity and price, then returns the total bill.
# def create_invoice(product_name, quantity, price_per_unit):
#     """
#     Calculate total bill for a product.
#
#     :param product_name: Name of the product (string)
#     :param quantity: Quantity purchased (int or float)
#     :param price_per_unit: Price per unit (float or int)
#     :return: Dictionary with product details and total bill
#     """
#     if quantity <= 0 or price_per_unit < 0:
#         raise ValueError("Quantity must be positive and price must be non-negative.")
#
#     total = quantity * price_per_unit
#
#     return {
#         "Product": product_name,
#         "Quantity": quantity,
#         "Price per Unit": price_per_unit,
#         "Total Bill": total
#     }
#
# # Example usage
# invoice = create_invoice("Laptop", 2, 55000)
#
# print("=== Invoice ===")
# print(f"Product: {invoice['Product']}")
# print(f"Quantity: {invoice['Quantity']}")
# print(f"Price per Unit: ₹{invoice['Price per Unit']}")
# print(f"Total Bill: ₹{invoice['Total Bill']}")

# 10.Create a Library Book function that accepts book details and prints them.
# def library_book(title, author, year, isbn):
#     """
#     Accepts and prints library book details.
#
#     :param title: Title of the book (string)
#     :param author: Author of the book (string)
#     :param year: Year of publication (int)
#     :param isbn: ISBN number (string or int)
#     """
#     if not title or not author or year <= 0:
#         raise ValueError("Invalid book details provided.")
#
#     print("=== Library Book Details ===")
#     print(f"Title : {title}")
#     print(f"Author: {author}")
#     print(f"Year  : {year}")
#     print(f"ISBN  : {isbn}")
#
# # Example usage
# library_book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "9780743273565")

# 11.Create a Hospital Patient function that accepts patient details and prints them.
# def hospital_patient(name, age, gender, patient_id, diagnosis):
#     """
#     Accepts and prints hospital patient details.
#
#     :param name: Patient's full name (string)
#     :param age: Patient's age (int)
#     :param gender: Patient's gender (string)
#     :param patient_id: Unique patient ID (string or int)
#     :param diagnosis: Diagnosis or reason for admission (string)
#     """
#     if not name or age <= 0 or not gender or not patient_id or not diagnosis:
#         raise ValueError("Invalid patient details provided.")
#
#     print("=== Hospital Patient Details ===")
#     print(f"Name      : {name}")
#     print(f"Age       : {age}")
#     print(f"Gender    : {gender}")
#     print(f"Patient ID: {patient_id}")
#     print(f"Diagnosis : {diagnosis}")
#
# # Example usage
# hospital_patient("John Doe", 45, "Male", "P12345", "Pneumonia")

# 12.Create an Employee ID Card function that accepts employee details and displays them.
# def employee_id_card(name, emp_id, department, designation, company):
#     """
#     Accepts and displays employee ID card details.
#
#     :param name: Employee's full name (string)
#     :param emp_id: Employee ID (string or int)
#     :param department: Department name (string)
#     :param designation: Job title/designation (string)
#     :param company: Company name (string)
#     """
#     if not name or not emp_id or not department or not designation or not company:
#         raise ValueError("All employee details must be provided.")
#
#     print("\n=== Employee ID Card ===")
#     print(f"Company     : {company}")
#     print(f"Name        : {name}")
#     print(f"Employee ID : {emp_id}")
#     print(f"Department  : {department}")
#     print(f"Designation : {designation}")
#     print("========================\n")
#
# # Example usage
# employee_id_card(
#     name="Alice Johnson",
#     emp_id="E1024",
#     department="IT",
#     designation="Software Engineer",
#     company="Tech Solutions Pvt Ltd"

# 13.Create a Flight Ticket function that accepts passenger details and prints the ticket.
# def flight_ticket(passenger_name, flight_number, origin, destination, date, seat_number):
#     """
#     Accepts and prints flight ticket details.
#
#     :param passenger_name: Passenger's full name (string)
#     :param flight_number: Flight number (string)
#     :param origin: Departure city/airport (string)
#     :param destination: Arrival city/airport (string)
#     :param date: Flight date (string in format DD-MM-YYYY)
#     :param seat_number: Seat number (string)
#     """
#     if not all([passenger_name, flight_number, origin, destination, date, seat_number]):
#         raise ValueError("All ticket details must be provided.")
#
#     print("\n=== Flight Ticket ===")
#     print(f"Passenger Name : {passenger_name}")
#     print(f"Flight Number  : {flight_number}")
#     print(f"From           : {origin}")
#     print(f"To             : {destination}")
#     print(f"Date           : {date}")
#     print(f"Seat Number    : {seat_number}")
#     print("=====================\n")
#
# # Example usage
# flight_ticket(
#     passenger_name="John Smith",
#     flight_number="AI202",
#     origin="New Delhi (DEL)",
#     destination="Mumbai (BOM)",
#     date="25-08-2026",
#     seat_number="12A"
# )

# 14.Create a Hotel Booking function that accepts customer details and displays the booking.
# def hotel_booking(customer_name, room_type, check_in, check_out, guests, booking_id):
#     """
#     Accepts and displays hotel booking details.
#
#     :param customer_name: Full name of the customer (string)
#     :param room_type: Type of room booked (string)
#     :param check_in: Check-in date (string in format DD-MM-YYYY)
#     :param check_out: Check-out date (string in format DD-MM-YYYY)
#     :param guests: Number of guests (int)
#     :param booking_id: Unique booking ID (string or int)
#     """
#     if not all([customer_name, room_type, check_in, check_out, guests, booking_id]):
#         raise ValueError("All booking details must be provided.")
#     if guests <= 0:
#         raise ValueError("Number of guests must be at least 1.")
#
#     print("\n=== Hotel Booking Confirmation ===")
#     print(f"Booking ID   : {booking_id}")
#     print(f"Customer Name: {customer_name}")
#     print(f"Room Type    : {room_type}")
#     print(f"Check-in     : {check_in}")
#     print(f"Check-out    : {check_out}")
#     print(f"Guests       : {guests}")
#     print("==================================\n")
#
# # Example usage
# hotel_booking(
#     customer_name="Emma Wilson",
#     room_type="Deluxe Suite",
#     check_in="10-09-2026",
#     check_out="15-09-2026",
#     guests=2,
#     booking_id="HBK20260810"
# )

# 15.Design your own real-world application using at least five functions.
# from datetime import datetime
#
# # Global dictionary to store bookings
# bookings = {}
#
#
# # 1. Function to book a room
# def book_room(booking_id, customer_name, room_type, check_in, check_out, guests, price_per_night):
#     if booking_id in bookings:
#         print(f"[ERROR] Booking ID {booking_id} already exists.")
#         return
#     if guests <= 0 or price_per_night <= 0:
#         print("[ERROR] Guests and price must be positive.")
#         return
#
#     bookings[booking_id] = {
#         "Customer Name": customer_name,
#         "Room Type": room_type,
#         "Check-in": check_in,
#         "Check-out": check_out,
#         "Guests": guests,
#         "Price per Night": price_per_night
#     }
#     print(f"[SUCCESS] Booking created for {customer_name} (ID: {booking_id})")
#
#
# # 2. Function to view booking details
# def view_booking(booking_id):
#     booking = bookings.get(booking_id)
#     if not booking:
#         print(f"[ERROR] No booking found with ID {booking_id}")
#         return
#     print("\n=== Booking Details ===")
#     for key, value in booking.items():
#         print(f"{key}: {value}")
#     print("=======================\n")
#
#
# # 3. Function to cancel a booking
# def cancel_booking(booking_id):
#     if booking_id in bookings:
#         del bookings[booking_id]
#         print(f"[SUCCESS] Booking ID {booking_id} has been cancelled.")
#     else:
#         print(f"[ERROR] No booking found with ID {booking_id}")
#
#
# # 4. Function to list all bookings
# def list_all_bookings():
#     if not bookings:
#         print("[INFO] No bookings available.")
#         return
#     print("\n=== All Bookings ===")
#     for booking_id, details in bookings.items():
#         print(f"ID: {booking_id} | Customer: {details['Customer Name']} | Room: {details['Room Type']}")
#     print("====================\n")
#
#
# # 5. Function to calculate total bill
# def calculate_bill(booking_id):
#     booking = bookings.get(booking_id)
#     if not booking:
#         print(f"[ERROR] No booking found with ID {booking_id}")
#         return
#     check_in_date = datetime.strptime(booking["Check-in"], "%d-%m-%Y")
#     check_out_date = datetime.strptime(booking["Check-out"], "%d-%m-%Y")
#     nights = (check_out_date - check_in_date).days
#     total_cost = nights * booking["Price per Night"]
#     print(f"[BILL] Total cost for booking ID {booking_id}: ₹{total_cost}")
#
#
# # ---------------- Example Usage ----------------
# book_room("B001", "Alice Johnson", "Deluxe Suite", "10-09-2026", "15-09-2026", 2, 5000)
# book_room("B002", "John Smith", "Standard Room", "12-09-2026", "14-09-2026", 1, 3000)
#
# view_booking("B001")
# list_all_bookings()
# calculate_bill("B001")
# cancel_booking("B002")
# list_all_bookings()
