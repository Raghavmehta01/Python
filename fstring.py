# # List of data entries
# data_entries = [
#     {"name": "Alice", "age": 30, "weight": 65.5},
#     {"name": "Bob", "age": 25, "weight": 75.0},
#     {"name": "Charlie", "age": 35, "weight": 68.5}
# ]

# # Iterate over the data entries and print each one using an f-string
# for entry in data_entries:
#     print(f"Name: {entry['name']}, Age: {entry['age']}, Weight: {entry['weight']} kg")



data_entries = [
    {"name": "Alice", "age": 30, "weight": 65.5},
    {"name": "Bob", "age": 25, "weight": 75.0},
    {"name": "Charlie", "age": 35, "weight": 68.5}
]

for entry in data_entries:
    print(f"name: {entry['name']} age: {entry['age'] * 2} weight:{entry['weight']}") 
    