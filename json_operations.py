import json

data = '{"var1":"Shivam", "var2":56}'
parsed = json.loads(data)

print(parsed['var1'])

json_string = json.dumps(data)
print(type(json_string))
print(json_string)
