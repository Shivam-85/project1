# read
my_file = open('sample.txt')

print(my_file.read())

print(my_file.read())

# reset the cursor
my_file.seek(0)
print(my_file.read())

my_file.seek(0)
print(my_file.readlines())

my_file.close()

# write

# Passing 'w+' lets us read and write to the file
my_file = open('sample.txt', 'w+')
my_file.write('This is a new line')

my_file.seek(0)
print(my_file.read())

my_file.close()

# append
my_file = open('sample.txt', 'a+')
my_file.write('\nThis is text being appended to test.txt')
my_file.write('\nAnd another line here.')

my_file.seek(0)
print(my_file.read())

my_file.close()

# iterating through a file

for line in open('sample.txt'):
    print(line)


