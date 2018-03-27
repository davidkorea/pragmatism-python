import requests
import webbrowser
import time

api = 'https://api.github.com/users/davidkorea/starred'
all_info = requests.get(api).json()
starred = []
for i in all_info:
    starred.append(i['id'])
# print(starred)
while True:
    info = requests.get(api).json()
    for i in info:
        if not i['id'] in starred:
            starred.append(i['id'])
            proj_full_name = i['full_name']
            page_url = 'https://github.com/'+ proj_full_name
            webbrowser.open(page_url)
    time.sleep(600)