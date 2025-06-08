"""
write a function that takes a list of integers and returns only the even numbers
checking even by using the modulo function, if reminder = 2 its even

"""

def get_evens(lst):
    evens = []
    for num in lst:
        if num % 2 == 0:
            evens.append(num)
    return evens

lst = [1,2,3,4]
evens_lst = get_evens(lst)
print(evens_lst)


   