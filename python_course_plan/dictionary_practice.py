student = {
    "name": "Uduakabasi",
    "age": 17,
    "course": "Software Engineering"
}

print(student["name"])
print(student.get("country", "Not specified"))
student.update({
    "country": "Nigeria",
    "level": 200
})
for key, value in student.items():
    print(key, ":", value)