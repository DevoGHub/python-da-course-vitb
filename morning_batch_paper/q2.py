print("Enter Student's name:")
name = input()
print("Enter the attendance for each of the days")
attendance = [None] * 5

for i in range(0,5):
    attendance[i] = input()

print("Attendance for", name, 'is', attendance)