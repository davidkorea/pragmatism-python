# 从 GitHub 上选出符合这些条件的项目：
# 1. 最近一周内发布的
# 2. Star 数大于 200
# 3. topic 是 blockchain
# 当出现时，发送手机推送

# get_info -> make_message -> push_it

import requests

def get_info_list():
    api = 'https://api.github.com/search/repositories?q='
    query = 'topic:blockchain'
    full_url = api+query
    print(full_url)
    info = requests.get(full_url).json()['items']
    return info

def make_message(info,last_week):
    star_count = info['stargazers_count']
    created_time = info['created_at']
    if star_count > 7000:
        if created_time > last_week:
            title = info['full_name']
            message = info['description']
            url = info['html_url']
            user = 'uo1tkj4duz7idytx342xseq5dtc6yg'
            token = 'ae72tphuwx71qxpab5nn1hz6f3ygx8'
            api = 'https://api.pushover.net/1/messages.json?'
            template = 'token={token}&user={user}&message={m}&title={t}&url={u}'
            query = template.format(
                token = token,
                user = user,
                m = message,
                t = title,
                u = url
            )
            full_url = api + query
            # print(full_url)
            return full_url

def push_it(url):
    if url is not None:
    # 可能有一个项目的html_url为None，导致最后一个会报错
        requests.post(url)
        print('done')

info_list = get_info_list()
result=[]
for i in info_list:
    message = make_message(i,'2013-12-20T13:05:46Z')
    push_it(message)
