"""
you're givem a list of numbers, for example [1,0,3]
your job is to return the number 103

okay so first you create an empty string
then you iterate through the loop
in every iteration,
convert the item to string and add it to your empty string
then outside the loop,
return your string
"""

def list_to_number(digits):
    required = ""
    for i in digits:
        required = required + str(i)
    return required

digits = [1,0,3]
number = list_to_number(digits)
print(number)


