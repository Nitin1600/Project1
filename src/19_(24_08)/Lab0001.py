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

import copy

# Original nested list
original = [[1, 2, 3], ["A", "B", "C"]]

# Create copies
shallow_copied = copy.copy(original)
deep_copied = copy.deepcopy(original)

# Modify a nested element in the shallow copy
shallow_copied[0][0] = 99

print("Original:", original)          # Output: [[99, 2, 3], ['A', 'B', 'C']] -> Changed!
print("Shallow:", shallow_copied)    # Output: [[99, 2, 3], ['A', 'B', 'C']]
print("Deep:", deep_copied)          # Output: [[1, 2, 3], ['A', 'B', 'C']]  -> Safe!


The primary difference between a shallow copy and
a deep copy is how they handle nested, mutable objects (like lists inside lists).
Shallow Copy: Creates a new object but inserts references to the original nested objects.
Changes to nested items affect both copies.
Deep Copy: Creates a new object and recursively copies all nested objects.
The two objects are entirely independent

Summary TableFeatureShallow Copy (copy.copy())
Deep Copy (copy.deepcopy())
Nested ObjectsShared between original and copyIndependently duplicatedMemory usageLow
(only copies the outer container)Higher (duplicates everything)SpeedFastSlower (especially for large/complex structures)
Best Used ForFlat collections or when sharing state is fineComplex, nested data structures where isolation is required