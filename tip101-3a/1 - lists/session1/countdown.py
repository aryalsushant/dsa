"""
two positive integers will be given. m and n. m>n. print numbers from m down to n
"""

def countdown(m,n):
    for i in range(m, n-1, -1):
        print(i)

countdown(5,1)
