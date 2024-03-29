import os
import requests



output = f'''
============================
    Authentication test
============================
request done at "/permissions"
| username=""
| password=""
expected result = 
actual result = 
==> 
'''
log_filename = 'api_test.log'
if not os.path.exists(log_filename):
    with open(log_filename, 'w'):  # Ensure file exists
        pass

def log_result(output):
    with open(log_filename, 'a') as file:
        file.write(output)

log_result(output)