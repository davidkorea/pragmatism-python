# get_info_list -> make_message -> push_it

from datetime import datetime
import requests

def get_info_list():
    api = 'https://api.github.com/search/repositories?q='
    query = 'topic:crawler+language:python+'
    # time = 'created:2018-03-10'
    time = 'created:'+ str(datetime.now()).split()[0]
    full_url = api+query+time
    info = requests.get(full_url).json()['items']
    print(full_url)
    return info

# get_info_list()
def make_message(info):
    title = info['name']
    message = info['description']
    url = info['html_url']
    user = 'uo1tkj4duz7idytx342xseq5dtc6yg'
    token = 'ae72tphuwx71qxpab5nn1hz6f3ygx8'
    api = 'https://api.pushover.net/1/messages.json?'
    template = 'token={token}&user={user}&title={t}&message={m}&url={u}'
    query = template.format(
        token = token,
        user = user,
        t = title,
        m = message,
        u = url,
        )
    full_url = api+query
    return full_url

def push_it(pushover_url):
    requests.post(pushover_url)
    print('done')

info_list = get_info_list()
if len(info_list)>=1:
    for i in info_list:
        message = make_message(i)
        push_it(message)
else:
    message = 'NO Update'
    user = 'uo1tkj4duz7idytx342xseq5dtc6yg'
    token = 'ae72tphuwx71qxpab5nn1hz6f3ygx8'
    api = 'https://api.pushover.net/1/messages.json?'
    template = 'token={t}&user={u}&message={m}'
    query = template.format(
        t = token,
        u = user,
        m = message,
    )
    pushover_url = api + query
    requests.post(pushover_url)
    print('no update')