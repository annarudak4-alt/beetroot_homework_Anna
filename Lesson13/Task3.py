def square_numbers(num_list_1):
     return [num ** 2 for num in num_list_1]
my_list_1 = [1,2,3,4,5]
my_list_squared = square_numbers(my_list_1)
print(my_list_squared)


def remove_negatives(num_list_2):
     return [num for num in num_list_2 if num > 0]
my_list_2 = [1, -2, 3, -4, 5]
my_list_negatives = remove_negatives(my_list_2)
print(my_list_negatives)
