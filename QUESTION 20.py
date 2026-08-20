# SPLIT LIST INTO TWO EQUAL PARTS ?

my_list = [1, 2, 3, 4, 5, 6]

mid = len(my_list) // 2

first = my_list[:mid]
second = my_list[mid:]

print(first)
print(second)