import os
import requests

# Base configuration
api_address = 'fastapi'
api_port = 8000
users = [('alice', 'wonderland', 200), ('bob', 'builder', 200), ('clementine', 'mandarine', 403)]

# Define the log directory and filename
log_directory = 'log'
log_filename = 'authentication.log'
log_filepath = os.path.join(log_directory, log_filename)

# Ensure the log directory exists
os.makedirs(log_directory, exist_ok=True)

# Create the log file if it doesn't exist
if not os.path.exists(log_filepath):
    with open(log_filepath, 'w'):  # Ensure file exists
        pass

# Logging function
def log_result(output):
    if os.environ.get('LOG') == 1:
        with open(log_filepath, 'a') as file:
            file.write(output)

for username, password, expected in users:
    r = requests.get(
        url=f'http://{api_address}:{api_port}/permissions',
        params={
            'username': username,
            'password': password
        }
    )
    test_status = 'SUCCESS' if r.status_code == expected else 'FAILURE'
    output = f'''
============================
    Authentication test
============================
request done at "/permissions"
| username="{username}"
| password="{password}"
expected result = {expected}
actual result = {r.status_code}
==>  {test_status}
'''
    print(output)
    log_result(output)