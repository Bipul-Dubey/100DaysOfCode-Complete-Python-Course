from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path="D:\software\chromedriver_win32\chromedriver.exe"
service=Service(chrome_driver_path)
driver=webdriver.Chrome(service=service)

web_url="https://en.wikipedia.org/wiki/Main_Page"
driver.get(web_url)

article_count=driver.find_element(By.CSS_SELECTOR,"#articlecount a")
# print(article_count.text)

# article_count.click()

all_portal=driver.find_element(By.PARTIAL_LINK_TEXT,"View history")   # find by a text link given on page
# all_portal.click()

search=driver.find_element(By.NAME,"search")
search.send_keys("python")
search.send_keys(Keys.ENTER)

# driver.quit()