from bs4 import BeautifulSoup,SoupStrainer
import requests
import telegram
from PageParser import Finder

class Parser:
    def Extracter(self,categorylink,category):
        self.link = "https://www.1mg.com" +categorylink
        self.category = category
        print(self.link)
        r2 = requests.get(self.link)
        soups = BeautifulSoup(r2.content,"html.parser")
        page_class = soups.find("div",{"class" : "col-xs-12 style__div-paginate___37OJx"})
        pagenos = page_class.find("ul",{"class" : "list-pagination"})
        pg_list = pagenos.find_all("li",{"class" : ""})
        last_page_no = pg_list[-1].text
        print(last_page_no)
        for i in range(1,int(last_page_no)+1):
            print(self.link +"?filter=true&pageNumber=" +str(i))
            object = Finder()
            object.Meds(self.link +"?filter=true&pageNumber=" +str(i),self.category)
