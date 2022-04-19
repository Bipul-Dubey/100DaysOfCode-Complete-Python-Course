from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import smtplib

GIVEN_UP_SPEED=50
GIVEN_DOWN_SPEED=100
CHROME_DRIVER_PATH="D:\software\chromedriver_win32\chromedriver.exe"

SENDER_EMAIL=""
SENDER_PASSWORD=""
RECEIVER_EMAIL=""

class InternetSpeedComplaint:
    def __init__(self,driver_path):
        service=Service(driver_path)
        self.driver=webdriver.Chrome(service=service)
        self.down_speed=0
        self.up_speed=0
        self.result_id=0
    def get_Internet_Speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.btn=self.driver.find_element(By.CLASS_NAME,"start-text")
        self.btn.click()
        sleep(60)
        self.result_id=self.driver.find_element(By.CSS_SELECTOR,".result-item-inline > div:nth-child(2) > a:nth-child(1)").text
        self.down_speed=self.driver.find_element(By.CLASS_NAME,"download-speed").text
        self.up_speed=self.driver.find_element(By.CLASS_NAME,"upload-speed").text
        self.driver.close()

    def send_Coplaint(self):
        self.connection=smtplib.SMTP("smtp.gmail.com",port=587)
        self.connection.starttls()
        self.connection.login(user=SENDER_EMAIL,password=SENDER_PASSWORD)
        self.connection.sendmail(from_addr=SENDER_EMAIL,to_addrs=RECEIVER_EMAIL,
                                 msg=f"Subject:Network issue\n\n"
                                     f"Why my downloading speed is {self.down_speed}Mbps "
                                     f"and uploading speed is {self.up_speed}Mbps "
                                     f"I'm paying for {GIVEN_DOWN_SPEED}Mbps downloading "
                                     f"and {GIVEN_UP_SPEED}Mbps uploading "
                                     f"and here is result I'd {self.result_id}")
        self.connection.close()


bot=InternetSpeedComplaint(driver_path=CHROME_DRIVER_PATH)
bot.get_Internet_Speed()
if float(bot.up_speed)<GIVEN_UP_SPEED or float(bot.down_speed)<GIVEN_DOWN_SPEED:
    bot.send_Coplaint()
