my_dict = {}

print(type(my_dict))

my_dict = {'key1': 123, 'key2': [12, 23, 33], 'key3': ['item0', 'item1', 'item2']}

print(my_dict['key3'])

my_dict['key2'].append(44)

print(my_dict)

my_dict['key4'] = {'Key41': 41, 'key42': 42}

my_dict2 =my_dict['key4']
print(my_dict2['key42'])
my_dict[1]=41



print(my_dict)

# return list of keys
print(my_dict.keys())
# return list of values
print(my_dict.values())

# return tuples of all items
print(my_dict.items())


new_dict = {"k1": { "ver" : { "v0" : "d1", "v1" :"d1", "v2": "d2" }}}
dict2=new_dict['k1']
dict1=dict2['ver']
print(dict1['v2'])


new_dict = my_dict.copy()
del new_dict['key2']
print(new_dict)
print(my_dict)

