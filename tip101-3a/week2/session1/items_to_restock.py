"""
a function takes in a dictionary that maps product names to their quantity
and an integer restock_threshold
we need to return a list of products whose values are less than the threshold
"""

def get_items_to_restock(products, restock_threshold):
    restock_items = []
    for k,v in products.items():
        if v < restock_threshold:
            restock_items.append(k)
    return restock_items

#test case
products = {"Product1": 10, "Product2": 2, "Product3": 5, "Product4": 3}
restock_threshold = 5

print(get_items_to_restock(products, restock_threshold))
