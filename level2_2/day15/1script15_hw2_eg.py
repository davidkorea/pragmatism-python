# coding:utf-8
import time
import csv
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# CSV文件路径
CSV_PATH = './weibo_ad.csv'
# 登录页面URL
LOGIN_URL = 'https://weibo.com'
# 开启浏览器
def start_chrome():
    # driver = webdriver.Chrome(executable_path='./chromedriver')
    driver = webdriver.Chrome()
    driver.start_client()
    return driver
# 生成GET请求的URL
def query(today):
    return f'http://s.weibo.com/weibo/python&xsort=hot&suball=1×cope=custom:{today}:&Refer=g'
# 滚动屏幕
def scroll_down(driver):
    time.sleep(5)
    html_page = driver.find_element_by_tag_name('html')
    for i in range(10):
        html_page.send_keys(Keys.END)
        time.sleep(1)
    time.sleep(5)
# 获取页面信息
def find_cards_info(driver):
    # cards_sel = '#Pl_Official_MyProfileFeed__21 > div > div'
    cards_sel = '#pl_weibo_direct > div > div.feed_lists.W_texta > div'
    cards = driver.find_elements_by_css_selector(cards_sel)
    info_list = []
    for card in cards:
        name_sel    = 'div > div.WB_feed_detail.clearfix > dl > div > div.content.clearfix > div.feed_content.wbcon > a.W_texta.W_fb'
        content_sel = 'div > div.WB_feed_detail.clearfix > dl > div > div.content.clearfix > div.feed_content.wbcon > p'
        time_sel    = 'div > div.WB_feed_detail.clearfix > dl > div > div.content.clearfix > div.feed_from.W_textb > a.W_textb'
        link_sel    = 'div > div.WB_feed_detail.clearfix > dl > div > div.content.clearfix > div.feed_from.W_textb > a.W_textb'
        relay_sel   = 'div > div.feed_action.clearfix > ul > li:nth-child(2) > a > span > em'
        comm_sel    = 'div > div.feed_action.clearfix > ul > li:nth-child(3) > a > span > em'
        like_sel    = 'div > div.feed_action.clearfix > ul > li:nth-child(4) > a > span > em'
        name = card.find_element_by_css_selector(name_sel).text
        print(name)
        content = card.find_element_by_css_selector(content_sel).text
        print(content)
        time = card.find_element_by_css_selector(time_sel).text
        print(time)
        link = card.find_element_by_css_selector(link_sel).get_attribute('href')
        print(link)
        relay = card.find_element_by_css_selector(relay_sel).text
        print(relay)
        comm = card.find_element_by_css_selector(comm_sel).text
        print(comm)
        like = card.find_element_by_css_selector(like_sel).text
        print(like)
        info_list.append([name, content, time, link, relay, comm, like])
    return info_list
# 翻页
def find_next(driver):
    next_sel = '#pl_weibo_direct > div > div.WB_cardwrap.S_bg2.relative > div > a'
    next_page = driver.find_elements_by_css_selector(next_sel)
    if next_page:
        return next_page[0].get_attribute('href')
# 保存数据到CSV文件
def save_csv(info):
    if os.path.exists(CSV_PATH):
        # 此处指定文件的编码格式为utf-8，否则可能会出现编码错误
        # 在打开csv文件的时候，需指定编码为utf-8，否则可能会显示乱码
        with open(CSV_PATH, 'a', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(info)
    else:
        with open(CSV_PATH, 'w+', encoding='utf-8') as f:
            writer = csv.writer(f)
            # CSV文件的表头
            writer.writerow(['用户名','微博内容', '微博时间', '微博链接', '转发量', '评论量', '点赞量'])
            writer.writerows(info)
# 登录页面
def login(driver, url):
    driver.get(url)
    time.sleep(25)
# 启动爬虫的函数
def run_crawler(driver, url):
    driver.get(url)
    scroll_down(driver)
    info = find_cards_info(driver)
    save_csv(info)
    next_page = find_next(driver)
    if next_page:
        run_crawler(driver, next_page)


today = input("请输入今天的日期：")
url = query(today)
driver = start_chrome()
login(driver, LOGIN_URL)
run_crawler(driver, url)