
# sel='#pl_common_searchTop > div.search_topic > div.m_topic > div.small_pic > div > p > span:nth-child(2)'
#sel = 'div > p.total > span:nth-child(2)'
# url= 'https://s.weibo.com/weibo/%2523%25E5%25A5%25A5%25E6%2596%25AF%25E5%258D%25A1%2523&Refer=STopic_box'
from selenium import webdriver
import time

url= 'https://s.weibo.com/weibo/%2523%25E5%25A5%25A5%25E6%2596%25AF%25E5%258D%25A1%2523&Refer=STopic_box'

def open_chrome():
    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.start_client()
    return driver

def find_info(driver):
    sel = 'div > p.total > span:nth-child(2)'
    elems = driver.find_elements_by_css_selector(sel)[0].text.replace("讨论","")
    return elems

driver = open_chrome()
driver.get(url)
time.sleep(10)
info = find_info(driver)
if info > "360万":
    print(info)
else:
    print('nothing new')