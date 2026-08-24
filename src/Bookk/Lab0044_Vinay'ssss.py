# words="Nitin"
# Count={}
# for char in words.lower():
#     if char in Count:
#         Count[char] += 1
#     else:
#         Count[char] = 1
# print(Count)

# Problem 1:
# (vinay)
#
# Scenario :
# ATM Machine Transaction
#
# Inputs :
#     1.    Amount to be withdrawn - int
#     2.    List of denominations available - list
#
#
# Expected Output :
# Dictionary of Denomination as Key and Count of each Denomination as Value, such that total of all should be equal to amount requested
#


# Constrains :
# For any amount entered, maximum number of nearest largest available denomination should be chosen.
# Example :
# If Amount entered is Rs.5,300, and all Denominations are available,
# Then, output dictionary will be like :
# {2000:2, 500:2, 200:1, 100:1},
#
# If Amount entered is 300,
# Output Dictionary will be like :
# {200:1, 100:1}
# If Denomination available is only 100, 50, then, Output Dictionary will be like :
# {100:3}

# def atm_withdrawal(s):
#     Available_denominations = [100, 200, 500, 2000]
#
#     if type(s) != int:
#         return "Input should be integer"
#
#     if s <= 0:
#         return "Input should be positive"
#
#     if s % 100 != 0:
#         return "Input should be multiples of 100"
#
#     two_thousand_count = s//2000
#     balance_after_two_thousand_count = s - 2000 * two_thousand_count
#     five_hundered_count = balance_after_two_thousand_count // 500
#     balance_after_five_hundered = balance_after_two_thousand_count - 500 * five_hundered_count
#     two_hundered_count = balance_after_five_hundered // 200
#     balance_after_two_hundered_count = balance_after_five_hundered - 200 * two_hundered_count
#     one_hundered_count = balance_after_two_hundered_count // 100
#     balance_after_one_hundered_count = balance_after_two_hundered_count - 100 * one_hundered_count
#
#     return (dict(two_thousand_count=f"{two_thousand_count}", five_hundered_count=f"{five_hundered_count}",
#                  two_hundered_count=f"{two_hundered_count}", one_hundered_count=f"{one_hundered_count}"))
#
# print(atm_withdrawal(5300.37))
#

