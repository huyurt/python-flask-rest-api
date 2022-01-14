friend_ages = {"Hudayfe": 12, "Yurt": 87, "HY": 58}
friend_ages["HY"] = 21
print(friend_ages)

friend_ages2 = [
    {"name": "Hudayfe", "age": 12},
    {"name": "Yurt", "age": 87},
    {"name": "HY", "age": 58},
]
print(friend_ages2[1]["name"])


student_attendance = {"Hudayfe": 98, "Yurt": 89, "HY": 99}
print(list(student_attendance.items()))
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

if "HY" in student_attendance:
    print(f"HY: {student_attendance['HY']}")

attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))
