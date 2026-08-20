# PYTHON PROGRAM FOR ROTATE A LIST BY K POSITION ?

my_list = [1, 2, 3, 4, 5]
k = 2

k = k % len(my_list)

rotated = my_list[-k:] + my_list[:-k]

print(rotated)