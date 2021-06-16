from selenium import webdriver
from time import sleep

from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path = "E:\ProgramData\ChromDriver\chromedriver.exe")

browser.get('https://www.baidu.com/')

sleep(2)

browser.set_window_size(1000, 800)

browser.refresh()

#ele = browser.find_element_by_xpath("//form[@name='f']/input")
ele = browser.find_element_by_xpath("//input[@id='kw']")
print(ele)

ele.clear()
ele.send_keys("python")
ele.send_keys(Keys.ENTER)

sleep(2)

browser.get_screenshot_as_file("E:\ProgramData\ChromDriver\paiduimg.png")

browser.close()
