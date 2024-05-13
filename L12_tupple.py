# immutable object with indexing
# good for grouping data

student = ("abhi",32,"male")

print(student.count("abhi"))
print(student.index("male"))

for x in student:
    print(x)

if "ABHI".lower() in student: #student.code()
    print("Abhi is here")