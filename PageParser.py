from bs4 import SoupStrainer,BeautifulSoup
import requests
import telegram
from MedsParser import MedsParser

class Finder:
    def Meds(self,link,category):
        self.link = link
        self.category = category
        r = requests.get(self.link)
        soups2 = BeautifulSoup(r.content,"html.parser")
        medicines_page = soups2.find_all("div",{"class" : "style__product-box___liepi"})
        for m in medicines_page:
            medicine = m.find("a").attrs["href"]
            object = MedsParser()
            object.Medicine("https://www.1mg.com" +medicine,self.category)



