# 1.Print numbers from 1 to 20 using a for loop.
# Print numbers from 1 to 20 using a for loop
# for num in range(1, 21):
#     print(num)

# 2.Print numbers from 20 to 1 using a while loop.
#     # Print numbers from 20 to 1 using a while loop
#     num = 20  # starting number
#
#     while num >= 1:
#         print(num)
#         num -= 1  # decrease by 1 each time

# 3.Print all even numbers from 1 to 50.
# # Print all even numbers from 1 to 50
# for num in range(2, 51, 2):  # start at 2, go up to 50, step by 2
#     print(num)

# 4.Print all odd numbers from 1 to 50.
# for num in range(1, 51, 2):  # start at 1, go up to 50, step by 2
#     print(num)

# 5.Find the sum of numbers from 1 to 100.
# total_sum = 0
#
# for num in range(1, 101):
#     total_sum += num  # add each number to total_sum
#
# print("Sum of numbers from 1 to 100 is:", total_sum)

# 6.Find the product of numbers from 1 to 10.
# product = 1  # start with 1 because multiplying by 0 would make everything 0
#
# for num in range(1, 11):
#     product *= num  # multiply each number
#
# print("Product of numbers from 1 to 10 is:", product)

# 7.Count the number of characters in a string without using len().
# text = input("Enter a string: ")
#
# count = 0
# for char in text:
#     count += 1  # increment count for each character
#
# print("Number of characters in the string is:", count)

# 8.Count the number of vowels in a string.
# Count the number of vowels in a string
# text = input("Enter a string: ")
#
# vowels = "aeiouAEIOU"  # both lowercase and uppercase vowels
# count = 0
#
# for char in text:
#     if char in vowels:
#         count += 1
#
# print("Number of vowels in the string is:", count)


# 9.Count the number of digits in a string.
# Count the number of digits in a string
# text = input("Enter a string: ")
#
# count = 0
# for char in text:
#     if char.isdigit():  # check if the character is a digit
#         count += 1
#
# print("Number of digits in the string is:", count)


# 10.Reverse a string using a loop.
# Reverse a string using a loop
# text = input("Enter a string: ")
#
# reversed_text = ""  # empty string to store reversed result
#
# # Loop through the string in reverse order
# for char in text:
#     reversed_text = char + reversed_text  # prepend each character
#
# print("Reversed string is:", reversed_text)

# 11.Find the largest number in a list.
# Find the largest number in a list
# numbers = [12, 45, 7, 89, 34, 167]
#
# # Check if the list is not empty
# if not numbers:
#     print("The list is empty.")
# else:
#     largest = numbers[0]  # assume first element is largest initially
#
#     for num in numbers:
#         if num > largest:
#             largest = num  # update largest if a bigger number is found
#
#     print("The largest number in the list is:", largest)

# 12.Find the smallest number in a list.
# Find the smallest number in a list
# numbers = [15, 3, 27, -5, 42, 0]
#
# # Check if the list is not empty
# if not numbers:
#     print("The list is empty.")
# else:
#     smallest = numbers[0]  # assume first element is smallest initially
#
#     for num in numbers:
#         if num < smallest:
#             smallest = num  # update smallest if a smaller number is found
#
#     print("The smallest number in the list is:", smallest)

# 13.Calculate the average of numbers in a list.
# Calculate the average of numbers in a list

# numbers = [10, 20, 30, 40, 50]
#
# # Check if the list is not empty
# if not numbers:
#     print("The list is empty. Cannot calculate average.")
# else:
#     total = 0
#     count = 0
#
#     # Sum all numbers and count them
#     for num in numbers:
#         if isinstance(num, (int, float)):  # ensure it's a number
#             total += num
#             count += 1
#         else:
#             print(f"Skipping non-numeric value: {num}")
#
#     if count > 0:
#         average = total / count
#         print("The average is:", average)
#     else:
#         print("No numeric values found in the list.")

# 14.Count positive and negative numbers in a list.
# Count positive and negative numbers in a list

# numbers = [10, -5, 0, 23, -8, 7, -1]
#
# # Initialize counters
# positive_count = 0
# negative_count = 0
#
# # Loop through the list
# for num in numbers:
#     if isinstance(num, (int, float)):  # Ensure it's a number
#         if num > 0:
#             positive_count += 1
#         elif num < 0:
#             negative_count += 1
#         # Zero is ignored (neither positive nor negative)
#     else:
#         print(f"Skipping non-numeric value: {num}")
#
# # Display results
# print("Positive numbers count:", positive_count)
# print("Negative numbers count:", negative_count)

# 15.Remove duplicate values from a list without using a set.
# numbers = [4, 2, 7, 4, 9, 2, 1, 7, 3, 3]
#
# unique_list = []  # to store unique values
#
# for num in numbers:
#     if num not in unique_list:  # check if already added
#         unique_list.append(num)
#
# print("Original list:", numbers)
# print("List without duplicates:", unique_list)

# 16.Count the frequency of each character in a string.
# text = "programming in python"
# char_freq = {}
#
# for char in text:
#     if char in char_freq:
#         char_freq[char] += 1
#     else:
#         char_freq[char] = 1
#
# # Display results
# print("Character frequencies:")
# for char, freq in char_freq.items():
#     print(f"'{char}': {freq}")

# 17.Count the frequency of each element in a list.
# Count the frequency of each element in a list

# items = [4, 2, 7, 4, 9, 2, 1, 7, 3, 3, 4]
#
# # Dictionary to store element frequencies
# freq_dict = {}
#
# for item in items:
#     if item in freq_dict:
#         freq_dict[item] += 1
#     else:
#         freq_dict[item] = 1
#
# # Display results
# print("Element frequencies:")
# for element, freq in freq_dict.items():
#     print(f"{element}: {freq}")

# 18.Find the second largest number in a list.
# def find_second_largest(numbers):
#     # Remove duplicates by converting to a set
#     unique_numbers = list(set(numbers))
#
#     # Check if there are at least two unique numbers
#     if len(unique_numbers) < 2:
#         return None
#
#     # Sort in descending order
#     unique_numbers.sort(reverse=True)
#
#     # Return the second element
#     return unique_numbers[1]
#
#
# # Example usage:
# data = [10, 20, 4, 45, 99, 99, 21]
# result = find_second_largest(data)
#
# if result is not None:
#     print(f"The second largest number in {data} is: {result}")
# else:
#     print("The list does not have a second largest number.")

# 19.Find the second smallest number in a list.
# def find_second_smallest(numbers):
#     # Remove duplicates
#     unique_numbers = list(set(numbers))
#
#     # Check if there are at least two unique numbers
#     if len(unique_numbers) < 2:
#         return None
#
#     # Sort in ascending order
#     unique_numbers.sort()
#
#     # Return the second element
#     return unique_numbers[1]
#
#
# # Example usage:
# data = [10, 20, 4, 45, 99, 4, 21]
# result = find_second_smallest(data)
#
# if result is not None:
#     print(f"The second smallest number in {data} is: {result}")
# else:
#     print("The list does not have a second smallest number.")

# 20.Merge two lists without using the + operator.
# Merge two lists without using the + operator

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
#
# # Create a new list and extend it with elements from both lists
# merged_list = []
#
# for item in list1:
#     merged_list.append(item)
#
# for item in list2:
#     merged_list.append(item)
#
# print("List 1:", list1)
# print("List 2:", list2)
# print("Merged list:", merged_list)


















