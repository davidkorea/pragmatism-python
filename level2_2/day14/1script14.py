# diving top aoto like
# unlike = button.Button.LikeButton.ContentItem-action
# like = button.Button.LikeButton.is-active.ContentItem-action


from selenium import webdriver
import time

url = 'https://www.zhihu.com/'
topic_url = 'https://www.zhihu.com/topic/19599283/hot'
def open_chrome():
    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.start_client()
    return driver

def get_topic():
    sel = 'button.Button.LikeButton.ContentItem-action'
    elems = driver.find_elements_by_css_selector(sel)
    return elems



driver = open_chrome()
driver.get(url)
time.sleep(20)
driver.get(topic_url)
topic = get_topic()
for t in topic:
    t.click()
    time.sleep(5)