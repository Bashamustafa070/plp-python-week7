# list_report.py

# 1. Start with this list in your code
items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

# 2. Loop through the list and print each item numbered
print("--- Numbered Items ---")
for index, item in enumerate(items, start=1):
    print(f"{index}. {item}")

# 3. Count how many item names have more than 4 letters
more_than_four_count = 0
for item in items:
    if len(item) > 4:
        more_than_four_count + 1 # wait, fix logic: