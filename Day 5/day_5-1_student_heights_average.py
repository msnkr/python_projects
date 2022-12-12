# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_students = 0
total_height = 0

for students in student_heights:
  total_students += 1

for height in student_heights:
  total_height += height

print(f'The average height of students is: {round(total_height / total_students)}')

################## using sum and len ###########################

# print(f'The average height os students is: {round(sum(student_heights)/len(student_heights))}')