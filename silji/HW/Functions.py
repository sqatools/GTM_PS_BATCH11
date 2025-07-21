def get_max_value(my_list):
    if not my_list:
        return None  # Return None if the list is empty
    max_val = my_list[0]  # Assume first element is max initially
    for val in my_list:
        if val > max_val:
            max_val = val
    return max_val

# Example usage
numbers = [10, 25, 5, 77, 30]
result = get_max_value(numbers)
print("Maximum value is:", result)