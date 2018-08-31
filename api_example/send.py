import requests
import json
from pprint import pprint


print('Making POST request to paradigms endpoint...\n')
get_token = requests.post('http://127.0.0.1:8000/api/token/', {'username': 'admin', 'password': 'adminpassword'})

print('Converting JSON text to python dictionary...\n')
token_response = json.loads(get_token.text)

print('Pulling access token...\n')
access_token = token_response['access']

headers = {}

print('Making GET request with access token - \n{}\n'.format(access_token))
headers['Authorization'] = 'Bearer ' + access_token 

r = requests.get('http://127.0.0.1:8000/paradigms/', headers=headers)


print('Pretty printed data ...  \n\n')
pprint(json.loads(r.text))






