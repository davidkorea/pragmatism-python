# coding:utf-8
import time
import csv
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# CSV文件路径
CSV_PATH = './weibo.csv'
# 登录页面URL
LOGIN_URL = 'https://weibo.com'
# 需要统计结果的页面的URL
BASE_URL = 'https://weibo.com/bgsxy'
# 开启浏览器
def start_chrome():
    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.start_client()
    return driver
# 生成GET参数
def query(start_time, end_time):
    return f'?is_ori=1&key_word=&start_time={start_time}&end_time={end_time}&is_search=1&is_searchadv=1#_0'
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
    cards_sel = '#Pl_Official_MyProfileFeed__21 > div > div'
    cards = driver.find_elements_by_css_selector(cards_sel)
    info_list = []
    for card in cards[2:]:
        content_sel = 'div:nth-child(1) > div.WB_detail > div.WB_text.W_f14'
        time_sel    = 'div:nth-child(1) > div.WB_detail > div.WB_from.S_txt2'
        link_sel    = 'div:nth-child(1) > div.WB_detail > div.WB_from.S_txt2 > a:nth-child(1)'
        relay_sel   = 'div.WB_feed_handle > div > ul > li:nth-child(2) > a > span > span > span > em:nth-child(2)'
        comm_sel    = 'div.WB_feed_handle > div > ul > li:nth-child(3) > a > span > span > span > em:nth-child(2)'
        like_sel    = 'div.WB_feed_handle > div > ul > li:nth-child(4) > a > span > span > span > em:nth-child(2)'
        content = card.find_element_by_css_selector(content_sel).text
        time = card.find_element_by_css_selector(time_sel).text
        link = card.find_element_by_css_selector(link_sel).get_attribute('href')
        relay = card.find_element_by_css_selector(relay_sel).text
        comm = card.find_element_by_css_selector(comm_sel).text
        like = card.find_element_by_css_selector(like_sel).text
        info_list.append([content, time, link, relay, comm, like])
    return info_list
# 翻页
def find_next(driver):
    next_sel = 'a.page.next'
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
            writer.writerow(['微博内容', '微博时间', '微博链接', '转发量', '评论量', '点赞量'])
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


start_time = input("请输入开始时间：")
end_time = input("请输入结束时间：")
url = BASE_URL+query(start_time, end_time)
driver = start_chrome()
login(driver, LOGIN_URL)
run_crawler(driver, url)