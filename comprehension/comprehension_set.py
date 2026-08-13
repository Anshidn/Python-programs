numbers = [1,4,5,4,7,2,5,2,3,4,5,6,7,8,9,10]
unique_numbers = {x for x in numbers}

even_numbers = {x for x in numbers if x%2==0}
print(unique_numbers)
print(even_numbers)