"""
takes a list of student name as a parameter
returns a dictionary like  student1:1, 
"""

def student_dictionary(student_names):
    students = {}
    for i in range(len(student_names)):
        students[student_names[i]] = i+1
    return students

#example test case
student_names = ["Ada Lovelace", "Tu Youyou", "Mae Jemison", "Rajeshwari Chatterjee", "Alan Turing"]

print(student_dictionary(student_names))