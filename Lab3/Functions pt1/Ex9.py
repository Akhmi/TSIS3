def unique_elements(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

# Example usage:
input_list = [1, 2, 2, 3, 3, 4, 5, 5]
result = unique_elements(input_list)
print("Original List:", input_list)
print("List with Unique Elements:", result)
#Original List: [1, 2, 2, 3, 3, 4, 5, 5]
#List with Unique Elements: [1, 2, 3, 4, 5]