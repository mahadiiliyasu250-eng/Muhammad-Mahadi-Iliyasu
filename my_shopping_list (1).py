# 1. Create an Empty List
my_shopping_list = []
print(f"Initial list: {my_shopping_list}")

# 2. Add Items
my_shopping_list.append("Apples")
my_shopping_list.append("Bread")
my_shopping_list.append("Milk")
print(f"After appends: {my_shopping_list}")

# 3. Insert Item
my_shopping_list.insert(1, "Eggs")
print(f"After insert: {my_shopping_list}")

# 4. Access Elements
print(f"Item at index 0: {my_shopping_list[0]}")
print(f"Last item: {my_shopping_list[-1]}")
print(f"Item at index 2: {my_shopping_list[2]}")

# 5. Slicing
print(f"First two items: {my_shopping_list[:2]}")
print(f"From index 2 to end: {my_shopping_list[2:]}")
print(f"Reversed list: {my_shopping_list[::-1]}")

# 6. Remove Item by Value
my_shopping_list.remove("Bread")
print(f"After removing Bread: {my_shopping_list}")

# 7. Remove Item by Index (pop)
popped_item = my_shopping_list.pop(0)
print(f"Popped item: {popped_item}")
print(f"Final shopping list: {my_shopping_list}")

# Extra: Length and Sorting
print(f"Number of items left: {len(my_shopping_list)}")
my_shopping_list.sort()
print(f"Sorted list: {my_shopping_list}")
