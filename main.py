def my_function(array):
    smallest = array[0]  # Initialize smallest to the first element
    for element in array:
        if element < smallest:
            smallest = element
    return smallest

ar = [1, 3, 5, 93481, 91834]

print(my_function(ar))