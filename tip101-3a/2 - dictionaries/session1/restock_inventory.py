"""
a function restock_inventory takes in two parameters 
current_inventory, a dictionary
restock_list, items to restock, also a dictionary
key is the item and value is how many of those items we have / need to restock

we need to return the updated dictionary

1. loop through the restock_list
2. if a key is present in current_inventory, add the restock value to the current value
3. if it is not present, append the key and the value in current inventory
4. return current inventory
"""
def restock_inventory(current_inventory, restock_list):
    for item in restock_list:
        if item in current_inventory:
            current_inventory[item] += restock_list[item]
        else:
            current_inventory[item] = restock_list[item]
    return current_inventory

#example test case
current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}

restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}

print(restock_inventory(current_inventory, restock_list))
