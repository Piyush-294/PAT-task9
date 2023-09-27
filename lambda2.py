my_list = [1, 2, "Hello", "World", 3]

# Use a lambda function to check if an element is an integer or a string
is_int_or_str = lambda x: isinstance(x, (int, str))

# Use the `all` function to check all elements in the list
result = all(map(is_int_or_str, my_list))

if result:
    print("All elements in the list are integers or strings.")
else:
    print("Not all elements in the list are integers or strings.")
