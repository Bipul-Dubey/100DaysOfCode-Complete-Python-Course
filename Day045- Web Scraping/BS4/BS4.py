from bs4 import BeautifulSoup
# import lxml

with open("website.html",encoding="utf8") as file:
    contents=file.read()

soup=BeautifulSoup(contents,"html.parser")          # use lxml instead of html.parser if not working

# print(soup.title)
# print(soup)
# print(soup.prettify())
# print(soup.h1.string)

li_tags=soup.find_all(name="li")    # Return list of all tags of given name
# print(li_tags)

a_tags=soup.find_all(name="a")

# for tag in a_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

#  select using id name
heading=soup.find_all(name="h1",id="name")

# select using class name
h3=soup.find_all(name="h3",class_="heading")
# for tag in h3:
#     print(tag.getText())

# select using selrctor tag
name=soup.select_one(selector="#name")
# print(name)
headings= soup.select(selector=".heading")
print(headings)