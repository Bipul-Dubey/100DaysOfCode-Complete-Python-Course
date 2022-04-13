import requests
from bs4 import BeautifulSoup


response=requests.get(url="https://news.ycombinator.com")
yc_web_page=response.text
# print(yc_web_page)

soup=BeautifulSoup(yc_web_page,"html.parser")

articles=soup.find_all(name="a",class_="titlelink")

article_texts=[]
article_links=[]
for article_tag in articles:
    text=article_tag.getText()
    article_texts.append(text)
    link=article_tag.get("href")
    article_links.append(link)

article_upvotes=[int(score.getText().split()[0]) for score in soup.find_all(name="span",class_="score")]
largest_index=article_upvotes.index(max(article_upvotes))

print(article_upvotes)
print(len(article_upvotes))
print(largest_index)
print(article_texts[largest_index])
print(article_links[largest_index])
