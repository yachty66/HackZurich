import os
import requests
import config


headers = {
    'Content-Type': 'application/json',
    'Authorization': config.key,
}

response = requests.get('https://www.googleapis.com/fitness/v1/users/me/dataSources', headers=headers)
print(response.json())