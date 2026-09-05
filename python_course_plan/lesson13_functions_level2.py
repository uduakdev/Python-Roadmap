# parameters and arguments in functions
# def greet(name):
#     print("Hello", name)
#
# greet("Uduakabasi")
# greet("Michael")
# greet(6)

# def introduce(name, age):
#     print(f"My name is {name}")
#     print("I am", age, "years old")
#
# introduce("Uduakabasi", 17)
# introduce("Angel", 18)

# def favorite_food(food):
#     print("My favorite food is", food)
#
# favorite_food("Afang soup")
# favorite_food("Jollof rice")
# favorite_food("Fried rice")

# def student_info(name, age, course):
#     print("Name:", name)
#     print("Age:", age)
#     print("Course:", course)
#
# sif = student_info("Uduakabasi", 17, "Software Engineering")
#
# print(sif)

# return value in functions
# def add(a, b):
#     return a + b
#
# result = add(5, 3)
#
# print(result)

# def student_info(name, age, course):
#     return name, age, course
#
# sif = student_info("Uduakabasi", 17, "Software Engineering")
#
# print(sif)
# print(type(sif))
#
# name, age, course = student_info(
#     "Uduakabasi", 17, "Software Engineering"
# )
#
# print(name)
# print(age)
# print(course)

# def calculate(a, b):
#     return a + b
#
# result = calculate(10, 5)
#
# print(result)
# print(result * 2)
# print(result + 100)

# def square(number):
#     return number * number
#
# answer = square(7)
#
# print(answer)

def add(a, b):
    return a + b

x = add(5, 10)
y = add(x, 20)

print(y)

# print() displays a value. return gives a value back to the caller.