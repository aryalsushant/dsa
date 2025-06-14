"""
take two dictionaries of product catalogs
return combination such that if one product exists in both, the price of second catalog will overwrite
price of first catalog
"""

def merge_catalogs(catalog1, catalog2):
    catalog = {}
    for product1 in catalog1:
        for product2 in catalog2:
            if product1 == product2:
                catalog[product1] = catalog2[product2]
            else:
                catalog[product1] = catalog1[product1]
                catalog[product2] = catalog2[product2]

    return catalog

#test case
catalog1 = {"apple": 1.0, "banana": 0.5}
catalog2 = {"banana": 0.75, "cherry": 1.25}
print(merge_catalogs(catalog1, catalog2))