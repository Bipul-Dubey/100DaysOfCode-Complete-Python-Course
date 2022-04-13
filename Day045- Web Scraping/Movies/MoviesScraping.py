import requests
from bs4 import BeautifulSoup

response=requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies_data=response.text

soup=BeautifulSoup(movies_data,"html.parser")
movies_title=soup.find_all(name="h3",class_="title")


titles=[title.getText() for title in movies_title]

titles.reverse()


with open("movies.txt","w",encoding="utf8") as file:
    for name in titles:
        file.write(f"{name}\n")

