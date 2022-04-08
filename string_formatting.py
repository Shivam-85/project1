# string formatting

# 1.formatting with placeholder

print("I am Going to inject %s here" % "Something")

print("I am going to inject %s text here ,and %s text here" % ("some", "more"))

print("My name is %s" % 'shivam')

print("My name is %r" % 'shivam')

# padding and precision of floating point number

print('Floating point numbers: %25.2f' % (13.144))

# 2. formatting with .format() method

print("the {2} {1} {0}".format('fox', 'brown', 'quick'))

print("A {p} saved is a {p} earned".format(p="penny"))

# {0:8}--> 0 is the index 8 is the format specifier
print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:9}'.format('Apples', 3.))
print('{0:8} | {1:9}'.format('Oranges', 10))

# {0:=<8} --> padding the whitespaces with filling character(=),left align(<)
print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Left', 'Center', 'Right'))

# 3. string literals

name = 'Shivam'
print(f"My name is {name}")

num = 23.45
print(f"My 10 character, four decimal number is:{num:10.4f}")