"""
goal is to call the function so that it prints out the following to the console (without calling the function
 more than once):

1 mississipi
2 mississipi
3 mississipi
4 mississipi
5 mississipi
"""

def count_mississippi(limit):
        for num in range(1, limit):
              print( f"{num} mississippi")
                
count_mississippi(6)