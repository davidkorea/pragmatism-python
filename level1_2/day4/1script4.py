# https://github.com/davidkorea/pragmatism-python
# https://api.github.com/repos/davidkorea/pragmatism-python
import requests
import webbrowser
import time

url = 'https://github.com/davidkorea/pragmatism-python'
api = 'https://api.github.com/repos/davidkorea/pragmatism-python'
all_info = requests.get(api).json()
# through the method '.json()' to transfer the json file to python dict format
last_update = None
# last_update = '2018-03-13T07:07:40Z'
cur_update = all_info['updated_at']

while True:
    if not last_update:
        last_update = cur_update

    if cur_update > last_update:
        webbrowser.open(url)
    else:
        print('No update yet')
    time.sleep(600)


