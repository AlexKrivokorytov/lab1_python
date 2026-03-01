warehouse_1 = [
    "EL1001", "EL1002", "EL1003", "EL1004", "EL1005",
    "FD2001", "FD2002", "FD2003",
    "HOM3001", "HOM3002", "HOM3003",
    "SP4001", "SP4002"
]

warehouse_2 = [
    "EL1004", "EL1005", "EL1006", "EL1007",
    "FD2003", "FD2004", "FD2005",
    "HOM3002", "HOM3004",
    "SP4002", "SP4003",
    "OF5001", "OF5002"
]

set_1 = set(warehouse_1)
set_2 = set(warehouse_2)

symmetric_difference = set_1 ^ set_2
unique_count = len(symmetric_difference)
union_products = set_1 | set_2
only_first = set_1 - set_2
intersection_list = list(set_1 & set_2)

def add_hyphen(article):
    letters = ""
    digits = ""
    for char in article:
        if char.isalpha():
            letters += char
        else:
            digits += char
    return letters + "-" + digits

sorted_all_products = sorted([add_hyphen(item) for item in union_products])

print("Symmetric difference:", symmetric_difference)
print("Number of unique products:", unique_count)
print("Products in at least one warehouse:", union_products)
print("Products only in warehouse 1:", only_first)
print("Products in both warehouses:", intersection_list)
print("Sorted formatted list:", sorted_all_products)
