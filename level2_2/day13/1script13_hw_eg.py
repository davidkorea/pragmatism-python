# coding:utf-8
import time
from selenium import webdriver
# 利用webdriver开启chrome浏览器
def start_chrome():
    # windows系统下，executable_path='./chromedriver.exe'
    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.start_client()
    return driver
# 访问页面，并获取需要的信息
def get_info(driver, url):
    # 访问页面
    driver.get(url)
    # 等待响应6秒
    time.sleep(6)
    # 利用chrome中的css选择器，获取到如下定位字符串
    sel = "#pl_common_searchTop > div.search_topic > div.m_topic > div.small_pic > div > p > span:nth-child(2)"
    elems = driver.find_elements_by_css_selector(sel)
    # 通过页面检查，获取的结果只有一个，所以直接用elems[0].text
    # 此时获取的内容是“讨论363万”，利用replace函数，将“讨论”两个字删掉
    result = elems[0].text.replace("讨论","")
    return result

url = "https://s.weibo.com/weibo/%2523%25E5%25A5%25A5%25E6%2596%25AF%25E5%258D%25A1%2523&Refer=STopic_box"
driver = start_chrome()
target = "370万"
# 每隔1200秒，监测一次
while True:
    result = get_info(driver, url)
    if result >= target:
        print(f'微博话题“奥斯卡”的讨论量已经达到{result}')
        break
    else:
        print(f'微博话题“奥斯卡”的讨论量还未突破{target}')
    time.sleep(1200)
print("Done!")