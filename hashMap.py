# example one:
students = {}
math = students["001"] = "John"
science = students["002"] = "Mike"
art = students["003"] = "Joy"
social_science = students["004"] = "Hanna"
print(science)
# example two:
"""
we have a list of students with their matriculation numbers in different subjects, 
and we want to keep track of how many subjects each student passed in the list.
"""
student_list = {}
students_id = ["001", "002", "003", "001", "002"]
for student in students_id:
   if student in student_list:
       student_list[student] += 1
   else:
       student_list[student] = 1
for student_id, score in student_list.items():
   print("id", student_id + ": " + str(score))