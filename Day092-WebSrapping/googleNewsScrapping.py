from bs4 import BeautifulSoup
import requests

topic=input("Enter Your Interest topic here: ")
response=requests.get(url=f'https://news.google.com/search?q={topic}&hl=en-IN&gl=IN&ceid=IN%3Aen')
news_web_page=response.text

soup=BeautifulSoup(news_web_page,'html.parser')

articles=soup.find_all(name='a',class_='DY5T1d')

all_articles=[]
data={}
for article in articles:
    heading=article.getText()
    link=f"https://news.google.com/{article.get('href')}"
    data={'heading':heading,'link':link}
    all_articles.append(data)

for news in all_articles:
    print(news)
