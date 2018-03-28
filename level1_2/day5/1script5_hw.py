import requests

api = 'https://api.github.com/search/repositories?q=language:python'
api_info = requests.get(api).json()['items']
for i in api_info:
    # print(type(i['size']))
    if i['size'] > 200:
        # print(i['full_name'])
        if i['created_at'] > '2012-03-17T21:00:06Z':
            url = 'https://github.com/'
            full_name = i['full_name']
            proj_url = url + full_name
            print(proj_url)






