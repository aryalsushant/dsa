"""
a function called calculate_gpa
we have to calculate the gpa and return it as a float
the function takes in a dictiionary as parameter which contains a course and grade received in that course

example: report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
print(calculate_gpa(report_card))
"A" = 4
"B" = 3
"C" = 2
"D" = 1
"F" = 0
then the gpa is the average of all numbers

so i'll iterate thru the dictionary first
then I'll make a list of all grades like A, B, C
I'll then create a float = 0
loop thru the list of grades and
use if statements to add to the float based on the grade
and return the float/length of list: grades
"""

def calculate_gpa(report_card):
    grades = report_card.values()
    gpa = 0
    for grade in grades:
        if grade == "A":
            gpa += 4
        elif grade == "B":
            gpa += 3
        elif grade == "C":
            gpa += 2
        elif grade == "D":
            gpa += 1
        else:
            gpa += 0
    return round((gpa/len(grades)),2)

#example test case
report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
print(calculate_gpa(report_card))