# clean_list.py
# Тестові дані для завдання "Чистий список"

prices = [
    ["iPhone 15", 35000],
    ["Samsung S24", 32000],
    ["Xiaomi 14", 21000],
    ["iPhone 15", 35000],
    ["Google Pixel 8", 29000],
    ["Samsung S24", 32000],
    ["OnePlus 12", 28000],
    ["Xiaomi 14", 21000],
    ["iPhone 14", 30000],
    ["Sony Xperia 5", 27000],
    ["Google Pixel 8", 29000],
    ["iPhone 15", 35000],
    ["Nokia G60", 18000],
    ["Samsung S23", 26000],
    ["Xiaomi Redmi Note 13", 15000],
    ["Samsung S23", 26000],
    ["OnePlus 12", 28000],
    ["iPhone 14", 30000],
    ["Sony Xperia 5", 27000],
    ["Xiaomi Redmi Note 13", 15000],
    ["Google Pixel 7", 25000],
    ["Google Pixel 7", 25000],
    ["Nokia G60", 18000],
]

seen = set()
i = 0

while i < len(prices):
    item = tuple(prices[i])
    if item in seen:
        prices.pop(i)
    else:
        seen.add(item)
        i += 1

print(prices)