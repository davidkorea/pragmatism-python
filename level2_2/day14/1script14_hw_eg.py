# coding:utf-8
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# 打开Chrome浏览器
def start_chrome():
    # windows系统下，executable_path='./chromedriver.exe'
    driver = webdriver.Chrome(executable_path='./chromedriver')
    # driver = webdriver.Chrome()
    driver.start_client()
    driver.set_window_size(1500, 1500)
    return driver
# 打开登录界面
def login(driver, url):
    driver.get(url)
    time.sleep(25)
# 点赞函数
def click_like(driver, url, have_clicked):
    driver.get(url)
    # 等待页面加载
    time.sleep(20)
    # 获取每条微博的div标签
    weibo_sel = '#Pl_Official_MyProfileFeed__21 > div > div'
    weibo_elems = driver.find_elements_by_css_selector(weibo_sel)
    for w in weibo_elems:
        # 获取一条微博的时间
        time_sel = 'div.WB_feed_detail > div.WB_detail > div.WB_from.S_txt2 > a:nth-child(1)'
        weibo_time = w.find_elements_by_css_selector(time_sel)
        # 由于页面结构的原因，有的标签中没有时间信息，所以此处加了一个条件判断
        if len(weibo_time) == 1:
            weibo_time = weibo_time[0].text
        if weibo_time not in have_clicked:
            button_sel = 'div.WB_feed_handle > div > ul > li:nth-child(4) > a > span > span > span'
            button = w.find_elements_by_css_selector(button_sel)
            # 同样由于页面结构的原因，此处加了一个条件判断
            if len(button) == 1:
                button = button[0]
                # 微博页面上的“私信聊天”按钮，有时候会挡住点赞按钮，遇到这个问题的时候，
                # 我们先捕获异常，然后利用“下方向键”让页面自动滚动一点点，露出点赞按钮
                try:
                    button.click()
                except Exception:
                    html_page = driver.find_element_by_tag_name('html')
                    html_page.send_keys(Keys.DOWN)
                    button.click()
                have_clicked.append(weibo_time)
                # 微博的点赞速度过快会弹出提醒，所以时间间隔设置的长一点
                time.sleep(5)



login_url = 'https://weibo.com/'
weibo_url = 'https://weibo.com/bgsxy'
# 用时间做标识，来判断一条微博是否点赞过
have_clicked = []
driver = start_chrome()
login(driver, login_url)
while True:
    have_clicked = click_like(driver, weibo_url, have_clicked)
    time.sleep(1200)

