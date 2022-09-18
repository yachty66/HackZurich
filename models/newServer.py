import requests
import config 

headers = {
    # 'Content-Type': 'application/json',
    'Authorization': config.key,
}

json_data = {
    'model': 'text-davinci-002',
    'prompt': (
    "They cannot sleep. They tried but it seems not possible. They described their day as the following: Very busy at work. It was quite stressful. They said they are not able to sleep because of i have way to many thoughts in my head. A medical professional will tell them that they can try the following three things right now to fall asleep quickly despite the things mentioned above: 1."),
    'temperature': 0.7,
    'max_tokens': 100,
}

response = requests.post('https://api.openai.com/v1/completions', headers=headers, json=json_data)
print(response.json())
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"model": "text-davinci-002", "prompt": "Say this is a test", "temperature": 0, "max_tokens": 6}'
#response = requests.post('https://api.openai.com/v1/completions', headers=headers, data=data)