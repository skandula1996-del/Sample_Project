#WAP to create a new list containing only the numbers from a given list. my_list = [1, 2, 3, 'Jessa', 4, 5, 'Kelly', 'Jhon', 6]
my_list = [1, 2, 3, 'Jessa', 4, 5, 'Kelly', 'Jhon', 6]
numbers_only_list = []

for item in my_list:
    if isinstance(item, (int, float)):  # Checks if the item is an integer or a float
        numbers_only_list.append(item)

print(numbers_only_list)
