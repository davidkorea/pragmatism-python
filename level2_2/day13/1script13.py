from selenium import webdriver
import time

def open_chrome():
    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.start_client()
    return driver

def find_info(driver):
    sel = 'span > span.line.S_line1 > span >em:nth-child(2)'
    elems = driver.find_elements_by_css_selector(sel)
    return [int(el.text) for el in elems[1:]]

# driver = open_chrome()
# driver.get('https://weibo.com/5869525717/G2VASlH1o?from=page_1005055869525717_profile&wvr=6&mod=weibotime&type=comment')
# time.sleep(10)
# info = find_info(driver)
# print(info)
#
while True:
    driver = open_chrome()
    driver.get('https://weibo.com/5869525717/G2VASlH1o?from=page_1005055869525717_profile&wvr=6&mod=weibotime&type=comment')
    time.sleep(10)
    info = find_info(driver)
    rep,comm,like = info
    if rep > 30000:
        print('repost over '+str(rep))
        print(f'repost is over{rep}')
        break
    else:
        print('nothing new')
    time.sleep(1200)
print('done')