from bs4 import BeautifulSoup,SoupStrainer
import requests
import telegram
from CategoryParser import Parser

r = requests.get("https://www.1mg.com/categories/health-conditions-28")
strainer = SoupStrainer(class_="style__l1-category___1K8pS")
soup = BeautifulSoup(r.content,"html.parser",parse_only=strainer)
links =soup.find_all("div",{"class" : "style__l2-category___1OwSv"})

for link in links:
    category_link = link.find("a").attrs["href"]
    category_text = link.find("a").text
    object = Parser()
    object.Extracter(categorylink=category_link,category=category_text)
    print(category_text)
    print()
