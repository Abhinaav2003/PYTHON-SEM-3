# COUNT THE FREQUENCY OF EACH ELEMENT IN A LIST ?

my_list = [1, 2, 2, 3, 3, 3, 4, 4]

frequency = {}

for x in my_list:
    if x in frequency:
        frequency[x] += 1
    else:
        frequency[x] = 1

print(frequency)