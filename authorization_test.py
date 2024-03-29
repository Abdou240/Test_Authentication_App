import os
import requests

# Base configuration
api_address = 'fastapi'
api_port = 8000
tests = [
    ('alice', 'wonderland', '/v1/sentiment', 'life is beautiful', 200),
    ('alice', 'wonderland', '/v2/sentiment', 'life is beautiful', 200),
    ('bob', 'builder', '/v1/sentiment', 'that sucks', 200),
    ('bob', 'builder', '/v2/sentiment', 'that sucks', 403),
]

# Define the log directory and filename
log_directory = 'log'
log_filename = 'authorization.log'
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
    test_status = 'SUCCESS' if r.status_code == expected else 'FAILURE'
    output = f'''
============================
    Authorization test
============================
request done at "{endpoint}"
| username="{username}"
| password="{password}"
| sentence="{sentence}"
expected result = {expected}
actual result = {r.status_code}
==>  {test_status}
'''
    print(output)
    log_result(output)
