import os
import requests

# Base configuration
api_address = 'fastapi'
api_port = 8000
tests = [
    ('alice', 'wonderland', '/v1/sentiment', 'life is beautiful', 1),
    ('alice', 'wonderland', '/v1/sentiment', 'that sucks', -1),
    ('alice', 'wonderland', '/v2/sentiment', 'life is beautiful', 1),
    ('alice', 'wonderland', '/v2/sentiment', 'that sucks', -1),
]

# Define the log directory and filename
log_directory = 'log'
log_filename = 'content.log'
log_filepath = os.path.join(log_directory, log_filename)

# Ensure the log directory exists
os.makedirs(log_directory, exist_ok=True)



def log_result(output):
    if os.environ.get('LOG') == '1':
        with open(log_filepath, 'a') as file:
            file.write(output)

for username, password, endpoint, sentence, expected in tests:
    r = requests.get(
        url=f'http://{api_address}:{api_port}{endpoint}',
        params={
            'username': username,
            'password': password,
            'sentence': sentence
        }
    )
    result = r.json()
    test_status = 'SUCCESS' if (result['score'] == expected) else 'FAILURE'
    output = f'''
============================
    Content test
============================
request done at "{endpoint}"
| username="{username}"
| password="{password}"
| sentence="{sentence}"
expected sentiment = {expected}
actual sentiment = {result['score']}
==>  {test_status}
'''
    print(output)
    log_result(output)
