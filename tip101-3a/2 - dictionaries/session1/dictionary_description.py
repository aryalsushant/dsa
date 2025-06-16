"""
def get_description(info, keys):
    for key in keys:
	    print(info[key])

so this function has a bug and i gotta find and fix it

when i run it, it gives a key error: salary in line 11

i will try putting a condition so that it prints none when salary is not found in info

yup that fixed it
"""

def get_description(info, keys):
    for key in keys:
        if key not in info:
             print("None")
        else:
	        print(info[key])
             
          
#test case
info = {"name": "Tom", "age": "30", "occupation": "engineer"}
keys = ["name", "occupation", "salary"]
get_description(info, keys)