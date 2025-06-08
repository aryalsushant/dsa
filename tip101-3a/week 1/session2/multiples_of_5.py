"""
printing all multiples of 5 between 1 and 100

using a range function: starting value, ending value
then print everyhing thats a multiple of 5 between the starting value and ending value
its not optimized tho

"""

def multiples_of_five():
    for num in range(0, 101):
        if num % 5 == 0:
            print(num)

multiples_of_five()
