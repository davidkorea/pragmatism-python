from wxpy import *
import csv

# get_info -> sed_msg

def get_info():
    file = open('./tst.csv','r',encoding='utf-8')
    reader = csv.DictReader(file)
    return [info for info in reader]

# get_info()
def make_msg(raw_info):
    msg = '{n} 님, 안녕하세요! 내일{t}에 {a}에서 {c}에 참석하시기 바랍니다. 회신 부탁드립니다. 감사합니다!'
    return [msg.format(n=info['name'],
                       t=info['time'],
                       a=info['address'],
                       c=info['course']) for info in raw_info]


def send(msg):
    bot = Bot()
    for i in msg:
        name = i.split(' ')[0]
        friend = bot.friends().search(name)
        if len(friend) ==1:
            friend[0].sned(i)
        else:
            print(name)
            print('Please check this name')
        # bot.self.send('Hi,wechat!')
        # bot.file_helper.send('Hi,file helper')


raw_info = get_info()
msg = make_msg(raw_info)
send(msg)