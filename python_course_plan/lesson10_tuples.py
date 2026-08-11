# fruits = ("Apple", "Banana", "Mango")
# print(fruits[1])
#
# birth_date = (26, 8, 2009)
# print(birth_date)
#
# Unpacking
# student = ("Uduakabasi", 16, "Software Engineering")
#
# name, age, course = student
#
# print(name)
# print(age)
# print(course)
#
# .count()
# fruits = ("Apple", "Banana", "Apple", "Mango", "Apple") #Example 1
#
# print(fruits.count("Apple"))
#
# numbers = (1, 2, 3, 2, 4, 2) #Example 2
#
# print(numbers.count(2))
#
# .index()
# fruits = ("Apple", "Banana", "Mango", "Banana")
#
# print(fruits.index("Banana"))
#
# len()
# numbers = (5, 10, 15, 20, 25, 30)
#
# print(len(numbers))
#
# Looping through a tuple
# fruits = ("Apple", "Banana", "Mango") #Example 1
#
# for fruit in fruits:
#    print(fruit)
#
# numbers = (10, 20, 30, 40) #Example 2
#
# for number in numbers:
#    print(number)
#
# numbers = (2, 4, 6)
#
# for number in numbers:
#     print(number * 2)

#Nested tuples
# students = (
#     ("John", 20),
#     ("Mary", 19),
#     ("David", 21)
# )
#
# print(students[2][0])

student = ("Uduakabasi", 16, "Software Engineering", "Nigeria")

print(student[0])
print(len(student))
print(student.index("Nigeria"))

name, age, course, country = student
print(name)
print(age)
print(course)
print(country)

numbers = (2, 4, 2, 6, 2, 8)

print(numbers.count(2))