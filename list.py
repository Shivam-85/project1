
my_list = ['one', 'two', 'three', 4.5]

# indexing and slicing

print(my_list[3])

print(my_list[1:])

print(my_list[:3])

print(my_list[:])

## concatenate

my_list += ['add new element']
print(my_list)

# list methods

my_list.append(4)
print(my_list)

my_list.pop()
my_list.pop(3)
print(my_list)

my_list.reverse()
print(my_list)

my_list.sort()
print(my_list)

# Nesting list
lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]
lst_3 = [7, 8, 9]

matrix = [lst_1, lst_2, lst_3]

print(matrix)

print(matrix[1][2])

# mutable
matrix[1][2] = 4
print(matrix)
