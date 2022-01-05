import json

python_value = {'name': 'Zophie', 'isCat': True,
                'miceCaught': 0, 'felineIQ': None}
json_value = json.dumps(python_value)
print(json_value)
