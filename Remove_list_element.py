def remove_elements(lst):
    indices_to_remove = [0, 4, 5]
    new_lst = [elem for i, elem in enumerate(lst) if i not in indices_to_remove]
    return new_lst


my_list = [10, 20, 30, 40, 50, 60, 71, 18, 49, 60]
result = remove_elements(my_list)
print(result)
