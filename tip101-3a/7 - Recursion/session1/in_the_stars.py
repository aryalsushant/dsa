"""
A recursive function is a function that calls itself within the body of the function.

Step 1: Copy the recursive function insert_stars() into Replit and run it.

Step 2: Then create another function insert_stars_iterative() that produces the same output without using recursion or 
the built-in join() method.

Compare your iterative (non-recursive) solution to the recursive solution provided. What is similar? What is different?
"""
def insert_stars(s):
    # If the string is empty or has only one character, return it as is
    if len(s) <= 1:
        return s
    # Otherwise, insert '*' between the first character and the rest, then recurse
    else:
        return s[0] + '*' + insert_stars(s[1:])
        
print(insert_stars('abc'))

def non_recursive(s):
    if len(s) <= 1:
        return s
    else:
        lst = []
        for char in s:
            lst.append(char)
            
        
        return "*".join(lst)

print(non_recursive('abc'))