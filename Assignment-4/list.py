# Store fruits using list of dictionaries
products = [
    {"name": "Apple", "stock": 15},
    {"name": "Banana", "stock": 6},
    {"name": "Mango", "stock": 4},
    {"name": "Orange", "stock": 12},
    {"name": "Grapes", "stock": 8}
]

print("Fruits with stock less than 10:\n")

for item in products:
    if item["stock"] < 10:
        print(item["name"], "- Stock:", item["stock"])
