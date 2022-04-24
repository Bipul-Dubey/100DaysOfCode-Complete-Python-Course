import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

my_InstaId=""
my_InstaPassword=""
Instagram_ID=""         # id account to follow their follower
NUMBER_ACCOUNT_FOLLOWS=10
CHROME_DRIVER_PATH="D:\software\chromedriver_win32\chromedriver.exe"

class InstagramFollower:
    def __init__(self,CHROME_DRIVER_PATH):
        service=Service(CHROME_DRIVER_PATH)
        self.driver=webdriver.Chrome(service=service)
        self.scroll=0

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(10)
        username=self.driver.find_element(By.NAME,"username")
        username.send_keys(my_InstaId)
        password=self.driver.find_element(By.NAME,"password")
        password.send_keys(my_InstaPassword)
        password.send_keys(Keys.ENTER)

    def find_follower(self):
        self.driver.get(url=f"https://www.instagram.com/{Instagram_ID}/")
        followers=self.driver.find_element(By.XPATH,"/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
        followers.click()
        sleep(5)
        page = self.driver.find_element(By.XPATH,"//div[@class='isgrP']")
        for i in range(NUMBER_ACCOUNT_FOLLOWS//7):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", page)
            sleep(4)

    def follow(self):
        for i in range(1,NUMBER_ACCOUNT_FOLLOWS):
            try:
                follow_btn=self.driver.find_element(By.XPATH,f'/html/body/div[6]/div/div/div/div[2]/ul/div/li[{i}]/div/div[2]/button')
                follow_btn.click()
                sleep(1)
            except selenium.common.exceptions.ElementClickInterceptedException:
                confirm_cancel=self.driver.find_element(By.XPATH,"/html/body/div[7]/div/div/div/div[3]/button[1]")
                confirm_cancel.click()


bot=InstagramFollower(CHROME_DRIVER_PATH)
bot.login()
sleep(7)
bot.find_follower()
bot.follow()