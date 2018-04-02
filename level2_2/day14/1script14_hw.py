# url = https://weibo.com/bgsxy?from=myfollow_all
# open_chrome -> get_data -> click

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def open_chrome():
    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.start_client()
    driver.set_window_size(1500,1500)
    # if dont set broswer size ,
    # the chatting window will block the like button
    return driver

def login(driver,login_url):
    driver.get(login_url)
    time.sleep(60)


def get_info(driver,weibo_url,have_clicked):
    driver.get(weibo_url)
    time.sleep(60)
    wb_div = '#Pl_Official_MyProfileFeed__21 > div > div'
    wb_elems = driver.find_elements_by_css_selector(wb_div)
    for each_wb in wb_elems:
        wb_time = 'div.WB_feed_detail > div.WB_detail > div.WB_from.S_txt2 > a:nth-child(1)'
        each_wb_time = each_wb.find_elements_by_css_selector(wb_time)
        if len(each_wb_time)==1:
            each_wb_time = each_wb_time[0].text
        if each_wb_time not in have_clicked:
            button_sel = 'div.WB_feed_handle > div > ul > li:nth-child(4) > a > span > span > span'
            button = each_wb.find_elements_by_css_selector(button_sel)
            if len(button)==1:
                button=button[0]
                try:
                    button.click()
                except Exception:
                    html_page = driver.find_element_by_tag_name('html')
                    html_page.send_keys(Keys.DOWN)
                    button.click()
                have_clicked.append(each_wb_time)
                time.sleep(5)



login_url = 'https://weibo.com'
weibo_url = 'https://weibo.com/bgsxy'
have_clicked = []
driver = open_chrome()
login(driver,login_url)
get_info(driver,weibo_url,have_clicked)