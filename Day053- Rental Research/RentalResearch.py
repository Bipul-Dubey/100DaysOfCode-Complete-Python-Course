from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

GOOGLE_FORM="https://docs.google.com/forms/d/e/1FAIpQLSd3x3REOovHW7rCdsTuToOTc2eyjKIzT_4g_i0koH5xemFFCw/viewform?usp=sf_link"
RENT_SITE="https://www.99acres.com/"


class RentProperty:
    def __init__(self):
        service=Service("D:\software\chromedriver_win32\chromedriver.exe")
        self.driver=webdriver.Chrome(service=service)

    def property_search(self):
        self.driver.get(url=RENT_SITE)
        rent_btn=self.driver.find_element(By.XPATH,'//*[@id="inPageSearchForm_1"]')
        rent_btn.click()
        search=self.driver.find_element(By.XPATH, '//*[@id="keyword2"]')
        search.send_keys("kharar, mohali")
        location=self.driver.find_element(By.CLASS_NAME,'pageComponent ')
        location.click()
        searchbtn=self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/form/div/div[1]/div[2]/div/div/div[1]/div[2]/button/span')
        searchbtn.click()



rent=RentProperty()
rent.property_search()