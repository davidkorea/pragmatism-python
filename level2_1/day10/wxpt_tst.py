from wxpy import *

def wechat():
    bot = Bot()
    # myself = bot.self
    bot.self.send('Hi,wechat!')
    # frien = bot.friends().search(u'David.kor')[0]
    # print(frien)
    # embed()

wechat()