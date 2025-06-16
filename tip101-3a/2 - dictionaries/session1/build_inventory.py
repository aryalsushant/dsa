def build_inventory(product_names, product_prices):
    inventory = {}
    for i in range(len(product_names)):
        inventory[product_names[i]]=product_prices[i]
    return inventory

product_names = ["Apple", "Banana", "Orange"]
product_prices = [0.99, 0.50, 0.75]
print(build_inventory(product_names, product_prices))