import requests
data = {'phone':input('Enter Number: '),'message':input('Enter Message: '),'key': 'textbelt'}
resp = requests.post('https://textbelt.com/text',data = data)
print(resp.json())
