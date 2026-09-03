# does not print duplicates
# numbers = {1, 2, 2, 10, 3, 4, 5}
# print(numbers)
#
# # it is unordered
# fruits = {"apple", "banana", "cherry"}
# print(fruits)

# mixed = {"Uduakabasi", 17, True}
# print(mixed)

# Difference between empty dictionary and empty sets
# empty_1 = {}
# print(type(empty_1))
#
# empty_2 = set()
# print(type(empty_2))

# .add() method
# fruits = {"Apple", "Banana"}
# print(fruits)
#
# fruits.add("Mango")
#
# print(fruits)

# .add() won't create duplicates
# numbers = {4, 1, 3}
# print(numbers)
#
# numbers.add(4)
# numbers.add(2)
#
# print(numbers)

# .remove() method
# fruits = {"Apple", "Banana", "Mango"}
# print(fruits)
# fruits.remove("Banana")
#
# print(fruits)

# .remove() produces an error when the item doesn't exist
# fruits = {"Apple", "Banana", "Mango"}
#
# fruits.remove("Orange")

# .discard() method
# fruits = {"Apple", "Banana", "Mango"}
# print(fruits)
#
# fruits.discard("Banana")
#
# print(fruits)

# .discard() does not produce an error when the item doesn't exist
# fruits = {"Apple", "Banana", "Mango"}
# print(fruits)
#
# fruits.discard("Orange")

# in      → checks if something exists
# fruits = {"Apple", "Banana", "Mango"}
#
# print("Apple" in fruits)
# print("apple" in fruits)

# not in  → checks if something does NOT exist
# fruits = {"Apple", "Banana", "Mango"}
#
# print("Apple" not in fruits)
# print("apple" not in fruits)

# union of sets
# boys = {"John", "David", "Mike"}
# girls = {"Mary", "Jane", "Sarah"}
#
# together = boys.union(girls)
# print(together)

# python_students = {"John", "Mary", "David"}
# java_students = {"David", "Sarah", "John"}

# all_students = python_students.union(java_students)
#
# print("Python students:", python_students)
# print("Java students:", java_students)
# print("All students:", all_students)
# all_students = python_students | java_students
#
# print(all_students)

# intersection of sets
# python_students = {"John", "Mary", "David"}
# java_students = {"David", "Sarah", "John"}
#
# common = python_students.intersection(java_students)
#
# print(common)

# boys = {"John", "David", "Mike", "Chris"}
# football_players = {"Mike", "Chris", "Sarah"}
#
# football_boys = boys.intersection(football_players)
#
# print("Boys:", boys)
# print("Football players:", football_players)
# print("Boys who play football:", football_boys)

# difference in sets
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
#
# result = A.difference(B)
#
# print(result)
# print(A - B)
# print(A - B - result)

# python_students = {"John", "Mary", "David", "Peter"}
# java_students = {"David", "Peter", "Sarah"}
#
# result = python_students.difference(java_students)
#
# print(result)

# symmetric difference in sets
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
#
# result = A.symmetric_difference(B)
#
# print(result)
# print(A ^ B)