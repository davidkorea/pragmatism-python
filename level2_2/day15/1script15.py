from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import csv

'''
# *****************************
# ***** day15 + day15_hw1 *****
# *****************************
open_chrome -> search -> scroll_down -> find_next -> save 
'''

def open_chrome():
    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.start_client()
    return driver

def search(period):
    st,et = period.split('~')
    query = f'?is_ori=1&key_word=&start_time={st}&end_time={et}&is_search=1&is_searchadv=1#_0'
    return query

def scroll_down():
    html = driver.find_element_by_tag_name('html')
    for i in range(5):
        print(i)
        html.send_keys(Keys.END)
        time.sleep(5)


def get_info():
    cards_sel = 'div.WB_cardwrap.WB_feed_type'
    cards = driver.find_elements_by_css_selector(cards_sel)
    info_list = []
    for card in cards:
        time_sel = 'div.WB_from.S_txt2 > a:nth-child(1)'
        content_sel = 'div.WB_text.W_f14'
        link_sel = 'div.WB_from.S_txt2 > a:nth-child(1)'
        index_sel = 'span.line.S_line1 > span >  em:nth-child(2)' # 8
        time = card.find_element_by_css_selector(time_sel).text
        content = card.find_element_by_css_selector(content_sel).text
        link = card.find_element_by_css_selector(link_sel).get_attribute('href')
        rep,comm,like = card.find_elements_by_css_selector(index_sel)[1:]
        info_list.append([time,content,link,rep.text,comm.text,like.text])
    return info_list

def save(name,info_list):
    path = './'+name+'.csv' #name = period
    if not os.path.exists(path):
        with open(path,'w+',encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(info_list)
            print('create csv')
    else:
        with open(path, 'a', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(info_list)
            print('add to csv')

def find_next():
    next_sel = 'a.page.next'
    # next_page_url = driver.find_element_by_css_selector(next_sel).get_attribute('href')
    # can not know whether next page exsist or not . use find elements
    next_page = driver.find_elements_by_css_selector(next_sel)
    if next_page:
        return next_page[0].get_attribute('href')


def work_flow(period,base):
    if not base.endswith('feedtop'):
        query = search(period)
        time.sleep(5)
        wb_url = base+query
        driver.get(wb_url)
    else:
        driver.get(base)
    time.sleep(5)
    scroll_down()
    info = get_info()
    save(period,info)
    next_page = find_next()
    if next_page:
        work_flow(period,next_page)



base = 'https://weibo.com/bgsxy'
driver = open_chrome()
input()
work_flow('2017-11-01~2018-04-03',base)

# https://weibo.com/bgsxy