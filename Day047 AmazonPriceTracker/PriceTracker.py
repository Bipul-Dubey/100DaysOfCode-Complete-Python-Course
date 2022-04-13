from bs4 import BeautifulSoup
import requests
import smtplib

ACCEPT_LAN="en-US,en;q=0.5"
User_Agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"

header={
    "User-Agent":User_Agent,
    "Accept-Language":ACCEPT_LAN
}

response=requests.get(url="https://www.amazon.in/HP-Ultra-Slim-Multimedia-Experience-Resistance/dp/B09BBF2MKG/?_encoding=UTF8&pd_rd_w=T1jtd&pf_rd_p=fcac17e8-2a87-4225-8628-a80b57a1a106&pf_rd_r=9M7ATER3QH1XJRMZ1JJX&pd_rd_r=0d9a54c2-502f-4bcc-9c1a-b3131b341d7e&pd_rd_wg=a8lLl&ref_=pd_gw_cr_cartx&th=1",headers=header)

soup=BeautifulSoup(response.text,"html.parser")
price_tag=soup.find(name="span",class_="a-price-whole")
price=price_tag.getText().split(".")[0]

Buy_price="2,000"  # setting buy price

sender_email=""
sender_pass=""
receiver_email=""
if price<Buy_price:
    print("dropped")
    connection=smtplib.SMTP("smtp.gmail.com",port=587)
    connection.starttls()
    connection.login(user=sender_email,password=sender_pass)
    connection.sendmail(from_addr=sender_email,to_addrs=receiver_email,
                        msg=f"Subject:Price Dropped!!!\n\nCurrent Price is {price}")
    connection.close()
