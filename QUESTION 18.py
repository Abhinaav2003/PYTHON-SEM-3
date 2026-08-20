# REMOVE THE DUPLICATE ELEMENT FROM A LIST AND FROM A TUPLE ?

# 1. Remove duplicates from a List
# Using set()

my_list = [1, 2, 2, 3, 4, 4, 5]

my_list = list(set(my_list))

print(my_list)


# 2. Remove duplicates from a Tuple

my_tuple = (1, 2, 2, 3, 4, 4, 5)

unique_tuple = tuple(set(my_tuple))

print(unique_tuple)