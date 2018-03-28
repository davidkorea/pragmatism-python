# coding:utf-8
import requests
import time
# 函数实现发送信息的功能，信息内容体现在message参数中
def push_it(message):
    api = 'https://api.pushover.net/1/messages.json/'
    # 此处需要两个指定身份的字符串，需要在网站注册才能获得
    data = {
        'app_token':'abcdefg',  #需要替换成你的token
        'user':'abcdefg',     #需要替换成你的user id
        'message':message
    }
    requests.post(api, data)

def get_project(last_week, topic):
    api = 'https://api.github.com/search/repositories?q='
    query_created = 'created:>' + last_week
    query_topic =  'topic:' + topic
    r = requests.get(api + query_created + '+' + query_topic)
    return r.json()['items']

last_week = "2018-03-3T00:00:00Z"
topic = 'blockchain'
# 将符合条件的项目URL存入list变量中，便于查重
result = []
while True:
    # 获取项目列表，搜条件为最近一周、blockchain相关
    project_list = get_project(last_week, topic)
    for p in project_list:
        stars = p['stargazers_count']
        # 如果项目符合条件，则调用push_it函数，发送到手机上
        if stars > 200 and not p['html_url'] in result:
            message = 'The project '+ p['name'] + ' is qualified.' + ' URL: ' + p['html_url']
            push_it(message)
            result.append(p['html_url'])
    # 设置休眠，每10分钟运行一次
    time.sleep(600)
