from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
import os
import csv

'''
open_chrome -> search_input -> query -> scroll_down -> scrawler -> 
save -> find_next
'''

def open_chrome():
    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.start_client()
    return driver

def search_input(keyword):
    input_sel = 'div.gn_search_v2 > input.W_input'
    input_elem = driver.find_element_by_css_selector(input_sel)
    input_elem.send_keys(keyword,Keys.ENTER)

def query(keyword):
    today = datetime.today().date()
    return f'https://s.weibo.com/weibo/{keyword}&xsort=hot&suball=1&timescope=custom:{today}:{today}&Refer=g'
# https://s.weibo.com/weibo/python
# &xsort=hot&suball=1&timescope=custom:2018-04-04:2018-04-04&Refer=g

def scroll_down():
    html = driver.find_element_by_tag_name('html')
    for i in range(5):
        print(i)
        time.sleep(2)
        html.send_keys(Keys.END)

def crawler():
    cards_sel = 'div.WB_cardwrap.S_bg2.clearfix'
    cards = driver.find_elements_by_css_selector(cards_sel)
    info_list = []
    for card in cards:
        name_sel = 'a.W_texta.W_fb'
        time_sel = 'div.feed_from.W_textb > a.W_textb'
        content_sel = 'p.comment_txt'
        link_sel = 'div.feed_from.W_textb > a.W_textb'
        index_sel = 'div.feed_action.clearfix > ul > li'
        name = card.find_element_by_css_selector(name_sel).text
        time = card.find_element_by_css_selector(time_sel).text
        content = card.find_element_by_css_selector(content_sel).text
        link = card.find_element_by_css_selector(link_sel).get_attribute('href')
        rep,comm,like = card.find_elements_by_css_selector(index_sel)[1:]
        info_list.append([time,name,content,link,rep.text,comm.text,like.text])
    return info_list

def save(keyword,info_list):
    path = './' + keyword +'.csv'
    if not os.path.exists(path):
        with open(path,'w+',encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['time','name','content','link','repost','comment','like'])
            # write a row needs a list ['','','']
            writer.writerows(info_list)
            print('create csv')
    else:
        with open(path,'a',encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['-', '-', '-', '-', '-', '-', '-'])
            writer.writerows(info_list)
            print('add info')

def find_next():
    next_sel = 'a.page.next'
    next = driver.find_elements_by_css_selector(next_sel)
    if next:
        return next[0].get_attribute('href')

def work_flow(ad_query_url,keyword):

    driver.get(ad_query_url)
    time.sleep(10)
    scroll_down()
    info_list = crawler()
    save(keyword,info_list)
    next = find_next()
    if next:
        work_flow(next,keyword)

driver = open_chrome()
driver.get('https://weibo.com/u/5742726372')
input('Press ENTER to start')
keyword = input('search:')
time.sleep(5)
search_input(keyword)
time.sleep(5)
ad_query_url = query(keyword)
work_flow(ad_query_url,keyword)

