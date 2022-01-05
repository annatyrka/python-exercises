import json

string_of_JSON_data = '{"name":"Zophie", "isCat": true, "miceCaught":0,"felineIQ":null}'

json_data_as_Python_value = json.loads(string_of_JSON_data)
print(json_data_as_Python_value)
