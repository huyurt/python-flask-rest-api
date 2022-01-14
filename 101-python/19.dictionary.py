users = [
    (0, "Hudayfe", "password"),
    (1, "Yurt", "yurt123"),
    (2, "HY", "hy?."),
    (3, "username", "1234"),
]

username_mapping = {user[1]: user for user in users}

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]

if password_input == password:
    print("Correct")
else:
    print("Incorrect!")


student = {"name": "Hudayfe", "school": "Computing", "grades": (87, 93, 80)}

def avarage_grade(data):
    grades = data["grades"]
    return sum(grades) / len(grades)

print(avarage_grade(student))



def avarage_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        total += sum(student["grades"])
        count += len(student["grades"])
    return total / count

print(avarage_grade_all_students([student]))
