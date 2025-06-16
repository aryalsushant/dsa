"""
write a function keys v values
function takes a dictionary
adds all keys and adds all values
if sum of keys > sum of values, 
bla bla bla
"""

def keys_v_values(dictionary):
    keys = dictionary.keys()
    values = dictionary.values ()
    sum_keys = sum(keys)
    sum_values = sum(values)

    if sum_keys > sum_values:
        print("keys")
    elif sum_values > sum_keys:
        print("values")
    else:
        print("balanced")

#test case
dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
keys_v_values(dictionary1)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
keys_v_values(dictionary2)


