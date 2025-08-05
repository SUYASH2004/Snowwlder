import requests

API_KEY = 'AIzaSyB9L63ksh-IcbZl7su-W43VyZ0O4_8dbd4'

url = f'https://generativelanguage.googleapis.com/v1/models?key={API_KEY}'

response = requests.get(url)
print(response.json())
