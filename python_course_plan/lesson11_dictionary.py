student = {
    "name": "Uduakabasi",
    "age": 16,
    "course": "Software Engineering"
}

# print(student["name"])
# print(student["age"])
# print(student["course"])

student["age"] = 17 #change existing item in dictionary

# print(student["age"])

student["country"] = "Nigeria" # add item in dictionary

# print(student)

# del student["country"] #delete an item in dictionary

# print(student)

# .pop() "removes an item and returns the value that was removed"
# removed = student.pop("age")
#
# print(removed)
# print(student)

#checking if a key exists
# print("course" in student)
# print("state" in student)
#
# if "state" in student:
#     print(student["state"])
# else:
#     print("state not found")

# .keys() method
# print(student.keys())
#
# for key in student.keys():
#     print(key)

# .values() method
# print(student.values())
#
# for value in student.values():
#     print(value)

# .items() method "gives you both the keys and the values"
# print(student.items())
#
# for key, value in student.items():
#     print(f"{key}: {value}")

#looping through dictionary
# for value in student.values():
#     print(value)

# for key in student.keys():
#     print(key)

# for key in student:
#     print(key)

# for key, value in student.items():
#     print(key, ":", value)

#Nested Dictionaries
# students = {
#     "student1": {
#         "name": "John",
#         "age": 20
#     },
#     "student2": {
#         "name": "Mary",
#         "age": 19
#     }
# }
#
# print(students)
# print(students["student1"]["name"])
# print(students["student2"]["age"])

#.get() method
#print(student.get("school", "Not available"))

#.update() method
print(student)
student.update({
    "name": "Immortal One",
    "age": "???",
    "country": "Unknown???",
    "level" : 999
})
print(student)