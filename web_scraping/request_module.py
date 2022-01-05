import requests

# Response object
res = requests.get('http://automatetheboringstuff.com/files/rj.txt')
print(type(res))
print(res.raise_for_status())

# the Response object has a status_code attribute

print(res.status_code == requests.codes.ok)
print(len(res.text))
print(res.text[:250])
