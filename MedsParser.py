from bs4 import BeautifulSoup,SoupStrainer
import requests
import telegram
from PIL import Image
from Inserter import Inserter
import time

class MedsParser:
    def Medicine(self,link,category):
        try:
            self.link = link
            self.category = category
            print(self.link)
            #print(self.category)
            self.r = requests.get(self.link)
            time.sleep(1)
            self.soups3 = BeautifulSoup(self.r.content,"html.parser")
            if self.soups3.prettify().find("ProductTitle__product-title___3QMYH") != -1:
                self.med_name = self.soups3.find("h1",{"class" : "ProductTitle__product-title___3QMYH"}).text
                self.manufacturer = self.soups3.find("div", {"class" : "ProductTitle__manufacturer___sTfon"}).text
                try:
                    self.sale_price = self.soups3.find("div", {"style" : "font-size:30px;display:block;font-weight:bold;color:#212121;"}).text
                    self.mrp = self.soups3.find("span" , {"class" : "DiscountDetails__discount-price___Mdcwo"}).text
                except:
                    self.mrp = self.soups3.find("div", {"style" : "font-size:30px;display:block;font-weight:bold;color:#212121;"}).text
                    self.mrp = self.mrp.replace("MRP","")
                    self.sale_price = self.mrp
                try:
                    self.description = self.soups3.find("div" , {"class" : "ProductDescription__description-content___A_qCZ"}).text
                except:
                    self.description = "No Description Provided"
                try:
                    self.manu_address = self.soups3.find("div" ,{"class" : "style__manufacturer-footer___9K5EU"}).text
                    if self.manu_address.find("Manufacturer/Marketer Address") != -1:
                        self.address = self.manu_address.replace("Manufacturer/Marketer Address","")
                    else:
                        self.address = self.manu_address
                except:
                    self.address = "No Address Provided"

                print(self.med_name)
                print(self.description)
                print(self.mrp)
                print(self.sale_price)
                print(self.manufacturer)
                print(self.address)
                print()
            else:
                self.med_name = self.soups3.find("h1", {"class" : "DrugInfo__drug-name-heading___adCs-"}).text
                a1 = self.soups3.find("h2",{"class" : "DrugInfo__salt-info___1jmpf"}).text
                a2 = self.soups3.find("div", {"class" : "saltInfo DrugInfo__salt-name___2-9Vh"}).text
                b1 = self.soups3.find("h2",{"class" : "DrugInfo__title___2qdTY"}).text
                b2 = self.soups3.find("div", {"class" : "DrugInfo__uses___381Re"}).text
                c1 = self.soups3.find("h3",{"class" : "DrugUses__header___29NE-"}).text
                c2 = self.soups3.find("div", {"class" : "DrugUses__content___38C-l"}).text + " "
                d1 = self.soups3.find("h3", {"class" : "DrugSideEffects__header___3PuSv"}).text
                d2 = self.soups3.find("p", {"data-reactid" : "110"}).text
                e1 = self.soups3.find("h3",{"class" : "DrugConsumption__header___1Sqnj"}).text
                e2 = self.soups3.find("div", {"class" : "DrugConsumption__content___3mfDy"}).text
                g1 = self.soups3.find("h3",{"class" : "DrugProcess__header___2KJQt"}).text
                g2 = self.soups3.find("div", {"class" : "DrugProcess__content___232QU"}).text
                self.description = a1 +": " +a2 +"\n" +b1 +": " +b2 +"\n" +c1 +": " +c2 +"\n" +d1 +": " +d2 +"\n" +e1 +": " +e2 +"\n" +g1 +": " +g2
                self.address = self.soups3.find("div", {"class" : "style__manufacturer-footer___9K5EU"}).text
                self.mrp = self.soups3.find("div" , {"class" : "DrugPriceBox__price___dj2lv"}).text
                self.sale_price = self.mrp
                self.manufacturer = self.soups3.find("div", {"class" : "DrugInfo__company-name___39Abk"}).text
                print(self.med_name)
                print(self.description)
                print(self.mrp)
                print(self.sale_price)
                print(self.manufacturer)
                print(self.address)
                print()

            obj = Inserter()
            obj.InsertDoc(self.category,self.med_name,self.description,self.mrp,self.sale_price,self.manufacturer,self.address)
        except:
            pass 

